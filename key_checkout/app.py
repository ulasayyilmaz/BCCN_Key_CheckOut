import os
import json
import threading
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import openpyxl

app = Flask(__name__)
CORS(app)

EXCEL_FILE = "../checkouts.xlsx"
HEADER = ["Index", "Name", "Student ID", "Key ID", "Purpose", "Checkout Time", "Check-in Time", "PDF Filename"]

# Global lock for file operations and index assignment
file_lock = threading.Lock()

def get_next_index_and_write(row_data):
    """
    writes row_data (given in argument) to the excel sheet with the right index

    """
    with file_lock:
        if not os.path.exists(EXCEL_FILE):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(HEADER)
            next_index = 1
        else:
            try:
                # loads the spreadsheet
                workbook = openpyxl.load_workbook(EXCEL_FILE)
                sheet = workbook.active

                # Determine next index from the last row
                if sheet.max_row <= 1:
                    next_index = 1
                else:
                    # Read the last index (last row, first column)
                    last_index_val = sheet.cell(row=sheet.max_row, column=1).value
                    try:
                        next_index = int(last_index_val) + 1
                    except (ValueError, TypeError):
                        # Fallback if the cell value isn't a valid integer
                        next_index = sheet.max_row
            except Exception as e:
                raise Exception(f"Failed to load Excel file: {e}")
        
        # Prepend the index to the row_data
        full_row = [next_index] + row_data
        sheet.append(full_row)
        
        try:
            workbook.save(EXCEL_FILE)
        except Exception as e:
            raise Exception(f"Failed to save Excel file: {e}")
            
        return next_index


# flask is listening to local server,
# whenever http request posted, it receives the data 
# by request.get_json
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # gets data by get_json (posted via ngrok tunnel from netlify server)
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "Invalid or missing JSON payload"}), 400
            
        # checks for required fields
        required_fields = ["name", "student_id", "key_id", "purpose", "signature_b64"]
        
        for field in required_fields:
            if field not in data or not isinstance(data[field], str) or not data[field].strip():
                return jsonify({"success": False, "error": f"Missing or empty required field: '{field}'"}), 400
                
        # Record checkout time (server's local time)
        checkout_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Prepare row data from 
        row_data = [
            data["name"].strip(),
            data["student_id"].strip(),
            data["key_id"].strip(),
            data["purpose"].strip(),
            checkout_time,
            "",  # Check-in Time
            ""   # PDF Filename
        ]
        
        print("Writing to Excel...")
        # gets index and writes to excel file
        next_index = get_next_index_and_write(row_data)
        print("Done. Row index:", next_index)
        
        # returns json of the data with index
        return jsonify({"success": True, "index": next_index}), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

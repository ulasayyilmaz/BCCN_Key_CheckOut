import urllib.request
import urllib.error
import json

url = 'http://localhost:5000/submit'

data = {
    "name": "Test Student2",
    "student_id": "12345678",
    "key_id": "K-42",
    "purpose": "Working in the lab",
    "signature_b64": "dummy_base64_string_representing_png"
}

json_data = json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=json_data, headers={'Content-Type': 'application/json'})

print("Sending POST request to:", url)
print("Payload:", data)
print("-" * 40)

try:
    response = urllib.request.urlopen(req)
    status_code = response.getcode()
    response_body = response.read().decode('utf-8')
    
    print(f"Status Code: {status_code}")
    print(f"Response: {response_body}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error Status Code: {e.code}")
    print(f"Response: {e.read().decode('utf-8')}")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
    print("Is the Flask server running? Make sure to start it with: python app.py")
except Exception as e:
    print(f"An error occurred: {e}")

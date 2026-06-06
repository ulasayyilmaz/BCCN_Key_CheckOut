### What this system does

A digital key checkout system for BCCN Berlin. Students scan a QR code,
fill in a form on their phone, and sign digitally. The form data is saved
automatically to a spreadsheet on the coordinator's computer, and a PDF
of the submission (including the student's signature) is saved locally.
No student data is stored online.

---

### First-time setup (do this once)

**1. Install Python**
Download from https://python.org. During installation, check the box
that says "Add Python to PATH".

**2. Install ngrok**
For mac, "brew install ngrok"
Download from https://ngrok.com/download and install it.
Start a user account. 
Then run this command in the terminal:
  ngrok config add-authtoken YOUR_TOKEN
Your token is at: https://dashboard.ngrok.com/get-started/your-authtoken

**3. Run the startup file**
- Windows: double-click start.bat
- Mac: open Terminal, run `chmod +x start.command` once, then
  double-click start.command from Finder

Everything installs automatically on first run.

**4. Set up the QR code (one time only)**
Go to any free QR code generator (e.g. qr-code-generator.com).
Create a QR code pointing to:
  https://imaginative-boba-7db2a1.netlify.app
Print it and place it at the desk. This same QR code works for all
students and all keys — no need to ever regenerate it.

---

### Every time the office opens

1. Double-click start.bat (Windows) or start.command (Mac)
2. Wait until you see the word "Forwarding" in the terminal window
3. The system is ready. Do not close the terminal window.

---

### When a student checks out a key

- Student scans the QR code and fills in the form on their phone
- A new row appears automatically in checkouts.xlsx
- A PDF with their signature is saved in the pdfs/ folder
- The PDF filename matches the Index column in the spreadsheet
- Hand the student the key

---

### When a student returns a key

1. Open checkouts.xlsx
2. Find the student's row by name or key ID
3. Type the return date and time in the "Check-in Time" column
4. Save the file

---

### Backups (weekly)

Copy the key_checkout/ folder to a USB drive or university network
storage. The two critical items are:
- checkouts.xlsx
- pdfs/

These files are intentionally not stored online for privacy reasons.
The local backup is the only copy.

---

### Troubleshooting

**Nothing appears in Excel after a student submits:**
Check that the terminal window is still open. If it closed, restart
by double-clicking the startup file.

**The "Forwarding" line is gone from the terminal:**
Close the terminal window and double-click the startup file again.

**Student sees an error on their phone:**
Check the terminal window is open and showing "Forwarding". If not,
restart the startup file.

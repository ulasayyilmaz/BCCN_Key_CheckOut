# BCCN_Key_CheckOut
Digitizing Key Check Out system at Humboldt University Haus 6 BCCN Campus

#### start.command (Mac — double-click to run)
- Same behavior as start.bat, adapted for Mac/bash
- Must be chmod +x so it's executable on Mac

---

### 4. QR CODE GENERATOR

`generate_qr.py` — run once per key to generate a printable QR code:
- Usage: `python generate_qr.py K-042`
- Generates a QR code pointing to `https://your-netlify-url.netlify.app/?key=K-042`
- Base Netlify URL is a configurable constant at the top of the file
- Saves output as `qr_K-042.png` in the current directory
- Dependency: `pip install qrcode[pil]`

---

### 5. README.md

Write in plain, non-technical language. Include:

1. **First-time setup** — install Python, run the start script, deploy the form folder to Netlify, install and run ngrok, update the BACKEND_URL in index.html, generate QR codes for each key
2. **Daily use for the coordinator**:
   - Double-click `start.bat` (or `start.command`) to start the backend
   - Run ngrok and update the form URL if it has changed
   - When a student submits the form, a new row appears in `checkouts.xlsx` automatically
   - When a student returns a key, find their row in `checkouts.xlsx` and type the return time in the "Check-in Time" column, change "Status" to "RETURNED"
3. **Backups** — periodically copy the `key_checkout/` folder (especially `checkouts.xlsx` and `pdfs/`) to a USB drive or university network storage
4. **Updating the ngrok URL** — explain clearly that the free ngrok URL changes every restart, and show exactly which line in index.html to update

---

## KEY CONSTRAINTS

- PDFs are never uploaded anywhere — written only to `key_checkout/pdfs/` on the local machine
- The spreadsheet is local only — never synced to cloud
- All timestamps use server time, not client time
- The backend has no dashboard, no login, no admin UI — it is a background process only
- The student form must work on mobile (iOS and Android) without any app install
- Concurrent submission safety: use a file lock when assigning the index and writing to the spreadsheet
- The Excel file should remain openable by the coordinator in Microsoft Excel or LibreOffice at all times (do not lock the file permanently)

---

## DELIVERABLES

1. `key_checkout/app.py`
2. `key_checkout/start.bat`
3. `key_checkout/start.command`
4. `key_checkout/generate_qr.py`
5. `key_checkout/README.md`
6. `netlify-form/index.html`
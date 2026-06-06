@echo off
cd /d "%~dp0"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install it from
    echo https://python.org ^(check 'Add to PATH'^) and run this file again.
    pause
    exit /b
)

if not exist key_checkout_env (
    python -m venv key_checkout_env
)

call key_checkout_env\Scripts\activate.bat

pip install -r requirements.txt --quiet

where ngrok >nul 2>&1
if %errorlevel% neq 0 (
    echo ngrok is not installed. Please install it from https://ngrok.com/download
    echo then run: ngrok config add-authtoken YOUR_TOKEN
    pause
    exit /b
)

echo ================================================
echo BCCN Key Checkout System — Starting...
echo ================================================
echo Do not close this window while the office is open.
echo When you see 'Forwarding' below, the system is ready.
echo ================================================

start /B python app.py
timeout /t 2 /nobreak > nul

ngrok http --url=sequence-tackling-eccentric.ngrok-free.dev 5000

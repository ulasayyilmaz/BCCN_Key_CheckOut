#!/bin/bash

cd "$(dirname "$0")"

if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install it from"
    echo "https://python.org (check 'Add to PATH') and run this file again."
    exit 1
fi

if [ ! -d "key_checkout_env" ]; then
    python3 -m venv key_checkout_env
fi

source key_checkout_env/bin/activate

pip3 install -r requirements.txt --quiet

if ! command -v ngrok &> /dev/null; then
    echo "ngrok is not installed. Please install it from https://ngrok.com/download"
    echo "then run: ngrok config add-authtoken YOUR_TOKEN"
    exit 1
fi

echo "================================================"
echo "BCCN Key Checkout System — Starting..."
echo "================================================"
echo "Do not close this window while the office is open."
echo "When you see 'Forwarding' below, the system is ready."
echo "================================================"

# Kill any stale process already holding port 5000
STALE=$(lsof -ti :5000)
if [ -n "$STALE" ]; then
    echo "Cleaning up stale process on port 5000 (PID $STALE)..."
    kill -9 $STALE 2>/dev/null
    sleep 1
fi

# Start Flask and remember its PID
python3 app.py &
FLASK_PID=$!

# Ensure Flask is killed on exit (Ctrl+C, terminal close, or ngrok exit)
cleanup() {
    echo ""
    echo "Shutting down Flask (PID $FLASK_PID)..."
    kill $FLASK_PID 2>/dev/null
    wait $FLASK_PID 2>/dev/null
    echo "Flask stopped. Goodbye."
}
trap cleanup EXIT INT TERM

sleep 2

ngrok http --url=sequence-tackling-eccentric.ngrok-free.dev 5000

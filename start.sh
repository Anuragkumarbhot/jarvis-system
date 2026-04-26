#!/data/data/com.termux/files/usr/bin/bash

echo "Starting Jarvis Secure Server..."

cd ~/assistant

gunicorn \
  --workers 2 \
  --bind 0.0.0.0:5000 \
  --certfile certs/cert.pem \
  --keyfile certs/key.pem \
  dashboard:app


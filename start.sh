#!/data/data/com.termux/files/usr/bin/bash

echo "Starting Jarvis..."

pkill -9 -f dashboard.py

sleep 2

python ~/assistant/dashboard.py

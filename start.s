#!/data/data/com.termux/files/usr/bin/bash

# ===============================
# Jarvis Startup Script
# ===============================

echo "Starting Jarvis services..."

# Set Python path
export PYTHONPATH=$HOME/assistant

# Stop old processes safely
pkill -f voice_assistant.py
pkill -f dashboard.py

sleep 2

# Ensure logs directory exists
mkdir -p ~/assistant/logs

# ===============================
# Start Voice Assistant
# ===============================

nohup python -u \
~/assistant/voice/voice_assistant.py \
> ~/assistant/logs/assistant.log 2>&1 &

echo "Voice assistant started"

sleep 2

# ===============================
# Start Web Dashboard
# ===============================

nohup python -u \
~/assistant/dashboard.py \
> ~/assistant/logs/dashboard.log 2>&1 &

echo "Dashboard started"

echo "All services running"

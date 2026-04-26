# Jarvis — Offline AI Voice Assistant & IoT Automation System

Jarvis is a local AI-powered assistant designed to run on mobile devices using Termux.  
It provides voice interaction, IoT device control, camera streaming, and a secure web dashboard — all running locally without cloud dependency.

---

## Features

- IoT — ESP32 relay control
- Camera — Live camera streaming
- Login — Username / password authentication
- Dashboard — Web-based control panel
- AI — Offline language model support
- Automation — Task scheduling system
- Local — Runs fully offline
- Mobile — Designed for Android + Termux

---

## System Architecture

Mobile Device (Termux)
        │
        ▼
Flask Web Dashboard
        │
 ├── IoT Control (ESP32)
 ├── Camera Streaming
 ├── Voice Assistant
 └── Automation Engine

---

## Installation

Clone repository:

```bash
git clone https://github.com/Anuragkumarbhot/jarvis-system.git
cd jarvis-system

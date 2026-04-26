System Architecture

Android Device (Termux)

    |
    |
    Flask Dashboard
    |
    |---- IoT Controller
    |---- Camera Server
    |---- Authentication
    |---- System Monitor

Network Flow:

Browser → Dashboard → ESP32
Browser → Camera → Video
Dashboard → System Monitor

Ports:

Dashboard:

5000

Camera:

8080

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = "jarvis_secure_key"

USERNAME = "admin"
PASSWORD = "1234"

ESP32_IP = "192.168.1.50"

# -------------------------
# LOGIN
# -------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = request.form.get("username")
        pw = request.form.get("password")

        if user == USERNAME and pw == PASSWORD:
            session["user"] = user
            return redirect("/")

    return render_template("login.html")


def auth():
    return "user" in session


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# -------------------------
# HOME
# -------------------------

@app.route("/")
def index():

    if not auth():
        return redirect("/login")

    return render_template("index.html")


# -------------------------
# IOT CONTROL
# -------------------------

@app.route("/iot/<device>/<state>")
def iot(device, state):

    if not auth():
        return redirect("/login")

    try:

        url = f"http://{ESP32_IP}/{device}/{state}"
        requests.get(url, timeout=3)

        return jsonify({
            "device": device,
            "state": state,
            "status": "sent"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


# -------------------------
# CAMERA STREAM
# -------------------------

@app.route("/camera")
def camera():

    if not auth():
        return redirect("/login")

    return render_template("camera.html")


# -------------------------
# SYSTEM MONITOR
# -------------------------

@app.route("/system")
def system():

    battery = "unknown"

    if os.path.exists("/sys/class/power_supply/battery/capacity"):
        with open("/sys/class/power_supply/battery/capacity") as f:
            battery = f.read().strip()

    return jsonify({
        "cpu": "ok",
        "ram": "ok",
        "battery": battery
    })


# -------------------------
# START SERVER
# -------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

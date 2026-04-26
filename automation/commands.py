import os
import psutil

from automation.reminders import add_reminder
from automation.reminders import list_reminders


def handle_command(command):

    command = command.lower()

    # ================= WIFI =================

    if "turn on wifi" in command:

        os.system("svc wifi enable")

        return "WiFi turned on"

    if "turn off wifi" in command:

        os.system("svc wifi disable")

        return "WiFi turned off"

    # ================= FLASHLIGHT =================

    if "flashlight on" in command:

        os.system("termux-torch on")

        return "Flashlight on"

    if "flashlight off" in command:

        os.system("termux-torch off")

        return "Flashlight off"

    # ================= CAMERA =================

    if "open camera" in command:

        os.system(
            "am start -a android.media.action.IMAGE_CAPTURE"
        )

        return "Opening camera"

    # ================= YOUTUBE =================

    if "open youtube" in command:

        os.system(
            "am start "
            "-a android.intent.action.VIEW "
            "-d https://youtube.com"
        )

        return "Opening YouTube"

    # ================= BATTERY =================

    if "battery status" in command:

        try:

            battery = psutil.sensors_battery()

            if battery:

                percent = battery.percent

                return f"Battery is {percent} percent"

            return "Battery information unavailable"

        except:

            return "Battery information unavailable"

    # ================= SYSTEM INFO =================
    # Android-safe (no CPU access)

    if "system info" in command:

        try:

            ram = psutil.virtual_memory().percent

            return f"RAM usage {ram} percent"

        except:

            return "System information unavailable"

    # ================= REMINDERS =================

    if "remind me at" in command:

        try:

            parts = command.split(
                "remind me at"
            )[1]

            parts = parts.strip()

            time_part = parts.split(" ")[0]

            message = parts.replace(
                time_part,
                ""
            ).strip()

            add_reminder(
                time_part,
                message
            )

            return f"Reminder set at {time_part}"

        except:

            return "Could not set reminder"

    if "list reminders" in command:

        try:

            return list_reminders()

        except:

            return "No reminders found"

    # ================= TIME =================

    if "time" in command:

        try:

            return os.popen("date").read()

        except:

            return "Time unavailable"

    # ================= SHUTDOWN =================

    if "shutdown assistant" in command:

        return "EXIT"

    # ================= UNKNOWN =================

    return "Command not recognized"

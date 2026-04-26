import schedule
import time
import os

reminder_list = []

def speak(text):
    os.system(f'espeak "{text}"')

def add_reminder(time_str, message):

    def reminder_action():
        speak(message)

    schedule.every().day.at(time_str).do(
        reminder_action
    )

    reminder_list.append(
        (time_str, message)
    )

    print(
        f"Reminder set for {time_str}: {message}"
    )

def list_reminders():

    if not reminder_list:
        return "No reminders set"

    output = ""

    for t, m in reminder_list:
        output += f"{t} : {m}\n"

    return output

def start_reminder_loop():

    while True:

        schedule.run_pending()

        time.sleep(1)

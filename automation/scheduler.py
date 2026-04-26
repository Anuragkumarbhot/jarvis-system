import schedule
import time
import os

def morning_reminder():

    os.system('espeak "Good morning. Time to start your day"')


def night_task():

    os.system("termux-torch off")


def system_check():

    os.system('espeak "System running normally"')


def start_scheduler():

    # Daily reminder

    schedule.every().day.at("08:00").do(
        morning_reminder
    )

    # Night automation

    schedule.every().day.at("22:00").do(
        night_task
    )

    # Hourly check

    schedule.every().hour.do(
        system_check
    )

    print("Scheduler started")

    while True:

        schedule.run_pending()

        time.sleep(1)

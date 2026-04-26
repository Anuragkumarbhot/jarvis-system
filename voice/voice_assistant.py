import sys
import os

# Fix Python module path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import speech_recognition as sr
import subprocess
import time
import threading

from automation.commands import handle_command
from automation.scheduler import start_scheduler


# ================= CONFIG =================

MODEL_PATH = "/data/data/com.termux/files/home/assistant/models/tinyllama-1.1b-chat-v1.0-q4_k_m.gguf"
LLAMA_BIN = "/data/data/com.termux/files/home/llama.cpp/build/bin"

WAKE_WORD = "jarvis"


# ================= SPEAK =================

def speak(text):

    print("\nAssistant:", text)

    clean = text.replace('"', "").replace("'", "")

    os.system(f'espeak "{clean}"')


# ================= LISTEN =================

def listen():

    r = sr.Recognizer()

    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8

    try:

        with sr.Microphone(
            sample_rate=16000,
            chunk_size=1024
        ) as source:

            print("\nListening...")

            r.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = r.listen(
                source,
                timeout=10,
                phrase_time_limit=6
            )

        text = r.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except Exception as e:

        print("Audio error:", e)

        time.sleep(1)

        return ""


# ================= LLM =================

def ask_llama(prompt):

    try:

        cmd = [
            "./llama-cli",
            "-m",
            MODEL_PATH,
            "-p",
            prompt,
            "-n",
            "128",
            "-t",
            "4",
            "-c",
            "2048"
        ]

        result = subprocess.run(
            cmd,
            cwd=LLAMA_BIN,
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return "No response."

        return output

    except Exception as e:

        print("Model error:", e)

        return "Model error occurred."


# ================= MAIN =================

def main():

    print("\n=== Voice Assistant Started ===")

    # Start scheduler in background

    threading.Thread(
        target=start_scheduler,
        daemon=True
    ).start()

    speak("Assistant ready")

    while True:

        text = listen()

        if not text:
            continue

        # Shutdown

        if text in [
            "exit",
            "stop",
            "shutdown",
            "quit"
        ]:

            speak("Shutting down")

            sys.exit()

        # Wake word

        if WAKE_WORD in text:

            speak("Yes")

            command = listen()

            if not command:
                continue

            # Try automation first

            result = handle_command(command)

            if result == "EXIT":

                speak("Shutting down")

                sys.exit()

            if result:

                speak(result)

            else:

                response = ask_llama(command)

                speak(response)

        time.sleep(0.5)


# ================= START =================

if __name__ == "__main__":

    main()

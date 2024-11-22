from core.recognizer import recognize_speech
from core.speaker import speak
from commands.system import open_application

class Assistant:
    def __init__(self):
        self.active = True

    def process_command(self):
        command = recognize_speech()
        if command:
            if "abre" in command:
                app_name = command.replace("abre", "").strip()
                speak(f"Abriendo {app_name}")
                open_application(app_name)
            else:
                speak("No reconozco ese comando.")

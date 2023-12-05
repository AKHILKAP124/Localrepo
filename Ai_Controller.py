import speech_recognition as sr
from time import sleep

class AI_Volume_Controller:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.current_volume = 50

    def recognize_speech(self):
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                command = command.lower()
            return command
        except Exception as e:
            print(f"Error: {e}")
            return ""

    def change_volume(self, change):
        self.current_volume += change
        if self.current_volume < 0:
            self.current_volume = 0
        elif self.current_volume > 100:
            self.current_volume = 100
        print(f"Volume changed to {self.current_volume}")

    def start(self):
        while True:
            command = self.recognize_speech()
            if "volume up" in command:
                self.change_volume(10)
            elif "volume down" in command:
                self.change_volume(-10)
            elif "mute" in command:
                self.change_volume(-self.current_volume)
            elif "unmute" in command:
                self.change_volume(self.current_volume)
            sleep(1)

volume_controller = AI_Volume_Controller()
volume_controller.start()
import speech_recognition as sr
from beepy import beep
import builtins

def play_sound():
    beep(sound="coin")

class SpeechToTextInputer:
    def __init__(self):
        self.r = sr.Recognizer()
    
    def readline(self, *args):
        while True:
            with sr.Microphone() as source:
                play_sound()
                audio = self.r.record(source, 4)
                print('\a')
            try:
                text = self.r.recognize_google(audio)
                if text:
                    return text
            except sr.UnknownValueError:
                print("Sorry you mushmouth try again")
            except sr.RequestError:
                print("Sorry I had troubling connecting Try again.")
            except Exception:
                print("I'm sorry please try again")
        
    def __enter__(self):
        self.original_input = builtins.input
        builtins.input = self.readline
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        builtins.input  = self.original_input

            

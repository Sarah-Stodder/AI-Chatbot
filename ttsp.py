import pyttsx3
import sys

# Build Context manager

class TextToSpeechPrinter:
    def __init__(self):
        self.engine = pyttsx3.init()
    
    
    def __enter__(self):
        # save our print function
        self.original_print = print
        

        #create our own print
        def tts_print(*args, **kwargs):
            # Convert all my args to strings
            
            text = " ".join(str(arg) for arg in args)
            

            # Speak the text
            self.engine.say(text)
            self.engine.runAndWait()
        
        #set the new print function to print out loud
        sys.stdout.write = tts_print


    def __exit__(self, exc_type, exc_value, traceback):
        # Restore the og print to the stdout
        sys.stdout.write = self.original_print



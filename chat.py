from ttsp import TextToSpeechPrinter
from stti import SpeechToTextInputer
import os
from bardapi import Bard
from dotenv import load_dotenv




load_dotenv()
os.environ.get('_BARD_API_KEY')
class ChatBot:
    def __init__(self):
        self.name = "BotFather"
        self.user_name = "User"
    
    def save_user_name(self, user_name):
        self.user_name = user_name
    
    def get_user_info(self):
        print("What is your name? ")
        name=input("")
        self.save_user_name(name)
        print(f"Welcome {name}")
    
    def get_response(self, user_input):
        bad_chars = [ "*","**" ]
        response = Bard().get_answer(user_input)['content']
        for i in bad_chars:
            response = response.replace(i, '')
        return response
        
        
    def start_chat(self):
        print(f"Welcome! I'm {self.name}")
        self.get_user_info()
        print("What can I do for you today?")
        while True:
            user_input = input("")
            if user_input.lower() == "quit":
                print("Bye! It was great chatting with you!")
                break
            
            response = self.get_response(user_input)
            print(response)

with TextToSpeechPrinter(), SpeechToTextInputer():
    chatbot = ChatBot()
    chatbot.start_chat()


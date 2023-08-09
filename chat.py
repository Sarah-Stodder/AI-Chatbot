from ttsp import TextToSpeechPrinter
from stti import SpeechToTextInputer
import os
from bardapi import Bard
from bardapi.constants import SESSION_HEADERS
from dotenv import load_dotenv
import requests




load_dotenv()

token = os.environ.get('COOKIE_1')
cookie2 = os.environ.get('COOKIE_2')
cookie3 = os.environ.get('COOKIE_3')


session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)
session.cookies.set("__Secure-1PSIDTS", cookie2)
session.cookies.set("__Secure-1PSIDCC", cookie3)


bard = Bard(token=token, session=session)
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
        bad_chars = [ "*","**","/"]
        response = bard.get_answer(user_input)['content']
        for i in bad_chars:
            response = response.replace(i, '')
        return response
        
        
    def start_chat(self):
        print(f"Hello! I'm {self.name}")
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

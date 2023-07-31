from fuzzywuzzy import fuzz
import re
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
        # fuzzy_match_threshold = 70 # can change this if needed

        # # Define our input phrases with their answers
        # predefined_inputs = [
        #     "Hello":f"Hi {self.user_name}!",
        #     "How are you?":"I'm am super awesome. Thanks for asking!",
        #     "Who are you?":f"I'm a chatbot my name is {self.name}",
        #     "How do you convince people?": "I'm gonna make them an offer they can't refuse",
        #     "What is your favorite food":"Oranges and olive oil",
        #     "What is the answer to Life Universe and Everything":"42",
        # ]

        # # Tokenize the user input
        # user_input_tokens = re.findall(r'\w+',user_input.lower())

        # best_match = None
        # best_match_ratio = 0

        # for input_phrase in predefined_inputs:
        #     #tokenize the predefined input keys
        #     input_phrase_tokens =  re.findall(r'\w+',input_phrase.lower())
            
        #     match_ratio = fuzz.partial_ratio(user_input_tokens, input_phrase_tokens)

        #     if match_ratio > best_match_ratio:
        #         best_match = input_phrase
        #         best_match_ratio = match_ratio
        #     print(best_match)
        
        #  # Gerenate our Response based on the best match
        # if best_match and best_match_ratio >=fuzzy_match_threshold:
        #     return predefined_inputs[best_match]
        # else:
        #     return "English? Do you speak it?"
        
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


from Chatbot import Chatbot
from config import APIKEY

if __name__ == "__main__":
    chatbot: Chatbot = Chatbot(apiKey=APIKEY)
    while True:
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit", "stop"]:
            break
        response = chatbot.chat(userInput)
        print("AI: ", response)
        
        
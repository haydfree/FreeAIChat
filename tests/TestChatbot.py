import unittest
from flaskr.Chatbot import Chatbot
from flaskr.config import APIKEY
import flaskr.ErrorHandler


class TestChatbot(unittest.TestCase):
        
    def setUp(self):
        self.chatbot: Chatbot = Chatbot(apiKey=APIKEY)
        self.chatbot.chat("test")
    
    def tearDown(self):
        del self.chatbot
        self.chatbot = None
        
    def testInvalidApiKey(self):
        with self.assertRaises(flaskr.ErrorHandler.InvalidApiKey):
            self.chatbot: Chatbot = Chatbot(apiKey="123")
            self.chatbot.chat("test")
        self.tearDown()
        
    def testInvalidPrompt(self):
        pass
    
    def testNullPrompt(self):
        pass
    
    def testEdgeCasePrompt(self):
        pass
    
    
        
    
        
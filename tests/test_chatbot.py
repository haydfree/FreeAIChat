import pytest
from flaskr.Chatbot import Chatbot
from flaskr.config import APIKEY


class TestChatbot:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.chatbot = Chatbot(apiKey=APIKEY)
        self.chatbot.chat("test")
        yield
        del self.chatbot

    def testInvalidApiKey(self):
        with pytest.raises(Exception):
            Chatbot(apiKey="123")

    def testInvalidClient(self):
        with pytest.raises(Exception):
            Chatbot(apiKey="123").chat("hello")

    def testChatResponse(self):
        response = self.chatbot.chat("How are you?")
        assert isinstance(response, str)
        assert response != ""

    def testAddValidPrompt(self):
        initialLength = len(self.chatbot.getPrompts())
        self.chatbot.addPrompt("New prompt")
        assert len(self.chatbot.getPrompts()) == initialLength + 1

    def testAddInvalidPrompt(self):
        with pytest.raises(Exception):
            self.chatbot.addPrompt(123)

    def testAddNullPrompt(self):
        with pytest.raises(Exception):
            self.chatbot.addPrompt(None)

    def testAddValidResponse(self):
        initialLength = len(self.chatbot.getResponses())
        self.chatbot.addResponse("New response")
        assert len(self.chatbot.getResponses()) == initialLength + 1

    def testAddInvalidResponse(self):
        with pytest.raises(Exception):
            self.chatbot.addResponse(123)

    def testAddNullResponse(self):
        with pytest.raises(Exception):
            self.chatbot.addResponse(None)

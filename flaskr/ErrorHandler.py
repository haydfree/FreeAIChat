import openai
from config import APIKEY


class InvalidApiKey(Exception):
    pass


class ErrorHandler:

    @staticmethod
    def validateApiKey(apiKey: str):
        try:
            openai.api_key = apiKey
        except openai.APIConnectionError:
            raise InvalidApiKey("API key is invalid")
        
    @staticmethod
    def validateClient(client: openai.OpenAI):
        try:
            openai.OpenAI(api_key=APIKEY)
        except:
            pass
            
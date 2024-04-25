from openai import OpenAI
from typing import List


class Chatbot:
    __apiKey: str
    __client: OpenAI
    __prompts: List[str]
    __responses: List[str]

    def __init__(
            self,
            apiKey: str,
    ):
        client = OpenAI(
                api_key=apiKey
            )
        self.__apiKey = apiKey
        self.setClient(client)
        self.setPrompts([])
        self.setResponses([])

    def getClient(self) -> OpenAI:
        return self.__client
    
    def setClient(
            self,
            client: OpenAI,
    ) -> None:
        self.__client = client
        
    def getPrompts(self) -> List[str]:
        return self.__prompts
    
    def setPrompts(
            self,
            prompts: List[str],
    ) -> None:
        self.__prompts = prompts
        
    def addPrompt(
            self,
            prompt: str,
    ) -> None:
        self.__prompts += prompt
        
    def getResponses(self) -> List[str]:
        return self.__responses
    
    def setResponses(
        self,
        responses: List[str],
    ) -> None:
        self.__responses = responses
        
    def addResponse(
        self,
        response: str,
    ) -> None:
        self.__responses += response
        
    def chat(
            self,
            prompt
    ) -> str:
        client: OpenAI = self.getClient()
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        ).choices[0].message.content
        
        self.addPrompt(prompt)
        self.addResponse(response)
        return response
        
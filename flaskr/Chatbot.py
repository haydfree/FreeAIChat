from openai import OpenAI
from typing import List
from flaskr.ErrorHandler import ErrorHandler


class Chatbot:
    __apiKey: str
    __client: OpenAI
    __prompts: List[str]
    __responses: List[str]

    def __init__(
            self,
            apiKey: str,
    ):
        self.__validateApiKey(apiKey)

        client = OpenAI(
            api_key=apiKey
        )
        self.__validateClient(
            client=client,
            apiKey=apiKey,
        )

        self.setPrompts([])
        self.setResponses([])

    def __validateApiKey(
            self,
            apiKey: str,
    ) -> None:
        ErrorHandler.validateApiKey(apiKey)
        self.__apiKey = apiKey

    def __validateClient(
        self,
        client: OpenAI,
        apiKey: str,
    ) -> None:
        ErrorHandler.validateClient(
            client=client,
            apiKey=apiKey,
        )
        self.setClient(client)

    def __validateStr(
            self,
            text: str,
            isPrompt: bool,
    ) -> None:
        ErrorHandler.validateStr(text)
        if isPrompt:
            self.__prompts.append(text)
        else:
            self.__responses.append(text)

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
        self.__validateStr(
            text=prompt,
            isPrompt=True,
        )
        
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
        self.__validateStr(
            text=response,
            isPrompt=False,
        )
        
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
        
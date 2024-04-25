import openai


class InvalidApiKey(Exception):
    pass


class InvalidClient(Exception):
    pass


class InvalidStr(Exception):
    pass


class ErrorHandler:
    @staticmethod
    def validateApiKey(
            apiKey: str,
    ) -> None:
        try:
            openai.OpenAI(api_key=apiKey)
        except Exception:
            raise InvalidApiKey("API key is invalid")
        
    @staticmethod
    def validateClient(
            client: openai.OpenAI,
            apiKey: str,
    ) -> None:
        try:
            if not isinstance(client, openai.OpenAI):
                raise InvalidClient("Client is invalid")
            c = openai.OpenAI(api_key=apiKey)
            _ = c.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "123",
                    }
                ],
                model="gpt-3.5-turbo",
            ).choices[0].message.content
        except Exception:
            raise InvalidClient("Client is invalid")

    @staticmethod
    def validateStr(
            text: str,
    ) -> None:
        if not isinstance(text, str):
            raise InvalidStr("Not a valid string")
            
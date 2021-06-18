
class BaseError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

class InvalidOptionError(BaseError):
    pass

class InvalidTokenError(BaseError):
    pass

class InvalidVoiceChannelError(BaseError):
    pass

class HTTPConnectionError(BaseError):
    pass

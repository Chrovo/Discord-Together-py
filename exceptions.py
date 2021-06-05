class InvalidOptionError(Exception):
    def __init__(self, errormessage):
        self.errormessage = errormessage
class InvalidTokenError(Exception):
    def __init__(self, errormessage):
        self.errormessage = errormessage
class InvalidVoiceChannelError(Exception):
    def __init__(self, errormessage):
        self.errormessage = errormessage
class HTTPConnectionError(Exception):
    def __init__(self, errormessage):
        self.errormessage = errormessage

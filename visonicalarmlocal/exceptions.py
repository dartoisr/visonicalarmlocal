class Error(Exception):
    """ Base class for other exceptions """
    pass

class RequestError(Error):
    """ Raised when the client is not registred. """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
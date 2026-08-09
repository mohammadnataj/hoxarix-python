class HoxarixError(Exception):
    """
    Base Hoxarix SDK exception.
    """
    pass


class HoxarixAuthenticationError(HoxarixError):
    """
    Authentication failed.
    """
    pass


class HoxarixConnectionError(HoxarixError):
    """
    Connection to Hoxarix API failed.
    """
    pass


class HoxarixRuntimeError(HoxarixError):
    """
    Runtime execution failed.
    """
    pass

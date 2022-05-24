
class BadResponse(Exception):
    """
    Non-200 response from API
    """
    pass

class AuthError(Exception):
    """"
    Empty or invalid API key
    """
    pass

class NoResultsError(Exception):
    """
    Missing results key
    """
    pass

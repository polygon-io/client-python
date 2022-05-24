
class PolyBadResponse(Exception):
    """
    Non-200 response from API
    """
    pass

class PolyAuthError(Exception):
    """"
    Empty or invalid API key
    """
    pass

class PolyMissingResults(Exception):
    """
    Missing results key
    """
    pass

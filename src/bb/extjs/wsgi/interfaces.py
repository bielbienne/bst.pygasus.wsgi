from zope import interface


class IRootDispatcher(interface.Interface):
    """ 
    """
    
    def __init__(self, request, response):
        """
        """
    
    def run(self):
        """
        """


class IRequest(interface.Interface):
    """ 
    """


class IResponse(interface.Interface):
    """
    """


class IExceptionHandler(interface.Interface):
    """ Generic Exception Handler.
    """
    def __call__(self, context):
        """ return an Exception of type werkzeug.exceptions.HTTPException.
        """
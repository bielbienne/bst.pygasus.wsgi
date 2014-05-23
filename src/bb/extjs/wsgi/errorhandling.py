import transaction

from bb.extjs.core import extjs
from bb.extjs.wsgi.interfaces import IExceptionHandler

from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import InternalServerError



@extjs.implementer(IExceptionHandler)
class DefaultExceptionHandler(extjs.Adapter):
    """ This adapter is for all exceptions types.
        It recreate the exceptions and send it as
        InternalServerError.
        
        IN FUTURE WE SHOULD REMOVE THE ERROR MESSAGE FOR THE WEBUSER !!
    """

    extjs.context(Exception)

    def __call__(self):
        transaction.abort()
        return InternalServerError(str(self.context))


@extjs.implementer(IExceptionHandler)
class DefaultHTTPExceptionHandler(extjs.Adapter):
    """ This is a default dummy adapter that do
        nothing else as return the same error.
    """
    extjs.context(HTTPException)

    def __call__(self):
        transaction.abort()
        return self.context
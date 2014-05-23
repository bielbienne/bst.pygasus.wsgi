from werkzeug import wrappers
from bb.extjs.core import extjs
from bb.extjs.wsgi import interfaces


@extjs.implementer(interfaces.IRequest)
class Request(wrappers.Request):
    pass


@extjs.implementer(interfaces.IResponse)
class Response(wrappers.Response):
    pass
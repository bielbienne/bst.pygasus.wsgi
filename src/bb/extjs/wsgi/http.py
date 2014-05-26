import webob
from bb.extjs.core import extjs
from bb.extjs.wsgi import interfaces


@extjs.implementer(interfaces.IRequest)
class Request(webob.Request):
    pass

@extjs.implementer(interfaces.IResponse)
class Response(webob.Response):
    pass
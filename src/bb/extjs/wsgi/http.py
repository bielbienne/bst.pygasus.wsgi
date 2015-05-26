import webob
from bb.extjs.core import ext
from bb.extjs.wsgi import interfaces


@ext.implementer(interfaces.IRequest)
class Request(webob.Request):
    pass


@ext.implementer(interfaces.IResponse)
class Response(webob.Response):
    pass

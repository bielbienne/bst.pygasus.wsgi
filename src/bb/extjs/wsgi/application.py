import transaction

from bb.extjs.wsgi import interfaces
from bb.extjs.wsgi.http import Request
from bb.extjs.wsgi.http import Response

from zope.component import queryMultiAdapter

from webob.exc import HTTPNotFound


class ExtJSApp(object):
    
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    
    def dispatch_request(self, request):
        name = request.path_info_peek()
        if not name:
            name = 'index'
        response = Response()
        dispatcher = queryMultiAdapter((request, response,), interfaces.IRootDispatcher , name)
        try:
            if dispatcher is None:
                raise HTTPNotFound('%s was not found' % name)
            transaction.begin()
            dispatcher()
            transaction.commit()

            return response
        except Exception as e:
            handler = interfaces.IExceptionHandler(e)
            return handler()
        #except RetryException as e:
        #
        # if we begin to work with a sql database we properly
        # need to work with a RetryException. Show zope.publisher as
        # example and implement it here,

import transaction

from bb.extjs.wsgi import interfaces
from bb.extjs.wsgi.http import Request
from bb.extjs.wsgi.http import Response

from zope.component import getAdapters
from zope.component import queryAdapter

from werkzeug.wsgi import responder
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import InternalServerError



class ExtJSApp(object):
    
    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    
    def dispatch_request(self, request):
        mapper = Map()
        response = Response()
        for name, dispatcher in getAdapters((request, response), interfaces.IRootDispatcher):
            mapper.add(Rule(dispatcher.target, endpoint=dispatcher))
            
        adapter = mapper.bind_to_environ(request.environ)
        try:
            transaction.begin()
            dispatcher, values = adapter.match()
            dispatcher()
            transaction.commit()
            return response
        except Exception as e:
            handler = interfaces.IExceptionHandler(e)
            return handler()
        #except RetryException as e:
        #
        # if we beginn to work with a sql database we properly
        # need to work with a RetryException. Show zope.publisher as
        # example and implement it here,

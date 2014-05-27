from zope.interface import implementer
from zope.component.interfaces import IObjectEvent


class IPreRequestProcessingEvent(IObjectEvent):
    """ send before the request is processed and
        before the transaction is beginning.
    """


@implementer(IPreRequestProcessingEvent)
class PreRequestProcessingEvent(object):
    def __init__(self, context, request):
        self.object = context
        self.request = request


class IPostRequestProcessingEvent(IObjectEvent):
    """ send after request processing and after transaction commit.
    """


@implementer(IPostRequestProcessingEvent)
class PostRequestProcessingEvent(object):
    def __init__(self, context, request):
        self.object = context
        self.request = request
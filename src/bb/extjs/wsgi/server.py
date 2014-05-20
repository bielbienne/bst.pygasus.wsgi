from waitress import serve
from paste.deploy import loadapp



# bin/paster serve parts/etc/deploy.ini
def make_app(global_conf={}, config='', debug=False):
    from bielbienne.csrgenweb.web import app
    return app


# bin/paster serve parts/etc/deploy.ini
def make_debug(global_conf={}, config='', debug=False):
    from bielbienne.csrgenweb.web import app
    app.debug = debug
    return app


def run(config=None):
    wsgi = loadapp('config:%s' % config)
    serve(wsgi)

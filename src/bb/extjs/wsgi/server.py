import configparser
from waitress import serve
from paste.deploy import loadapp

import zope.component.hooks
from zope.configuration import xmlconfig
from zope.configuration import config as zconfig

from bb.extjs.wsgi.application import ExtJSApp


def make_app(global_conf={}, config='', debug=False):
    zcmlconfigure(global_conf)
    return ExtJSApp()


def make_debug(global_conf={}, config='', debug=False):
    """ do nothing else at the moment as the function make_app!!
    """
    return make_app(global_conf, config, debug)


def run(config=None):
    wsgi = loadapp('config:%s' % config)
    serve(wsgi)


def zcmlconfigure(ini_conf):
    """ configuration for ZCML. The path to site.zcml must be 
        written in the ini-file and defined in the section
        'zcml' as 'path'.
    """
    parser = configparser.ConfigParser()
    parser.read(ini_conf['__file__'])
    zcmlpath = parser.get('zcml', 'path')

    # Hook up custom component architecture calls
    zope.component.hooks.setHooks()

    # Load server-independent site config
    context = zconfig.ConfigurationMachine()
    xmlconfig.registerCommonDirectives(context)
    context = xmlconfig.file(zcmlpath, context=context, execute=True)

    return context
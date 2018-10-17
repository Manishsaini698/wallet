
from pyramid.config import Configurator

def included(config):
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('signup','/signup')
    config.add_route('create','/create')
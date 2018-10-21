from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import groupfinder

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application."""
    
    config = Configurator(settings=settings)

    authn_policy = AuthTktAuthenticationPolicy(
        settings['secret'], callback=groupfinder,
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    config.include('pyramid_jinja2')
    config.include("pyramid_beaker")

    config.add_static_view('static', 'static', cache_max_age=3600)
 
    config.add_route('home', '/')
    config.add_route('login','/login')
    config.add_route('signup','/signup')
    config.add_route('createCus','/createCus')
    config.add_route('createMer','/createMer')
    config.add_route('otpLogin','/otpLogin')
    config.add_route('enterotp','/enterotp/{txn}')
    config.add_route('passLogin','/passLogin')
    config.add_route('otpVerify','/otpVerify/{txn}')  
    config.add_route('user','/user')  
    config.add_route('userTransaction','/userTransaction')   
    config.scan('wallet.views')
 
    return config.make_wsgi_app()

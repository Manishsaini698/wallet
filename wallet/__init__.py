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
    config.add_route('logout', '/logout')
    config.add_route('signup','/signup')    
    config.add_route('loginMer','/loginMer')
    config.add_route('createCus','/createCus')
    config.add_route('createMer','/createMer')
    config.add_route('otpLogin','/otpLogin')
    config.add_route('otpLoginL','/otpLoginL')
    config.add_route('enterOtpCus','/enterOtpCus')
    config.add_route('enterotpM','/enterotpM/{txn}')
    config.add_route('enterotpL','/enterotpL')
    config.add_route('enterotpMD','/enterotpMD/{txn}')
    config.add_route('enterOtpMer','/enterOtpMer')
    config.add_route('enterotp','/enterotp/{txn}')
    config.add_route('passLogin','/passLogin')
    config.add_route('passLoginMer','/passLoginMer')   
    config.add_route('otpVerify','/otpVerify/{txn}')
    config.add_route('otpVerifyM','/otpVerifyM/{txn}')
    config.add_route('otpVerifyL','/otpVerifyL')
    config.add_route('otpVerifyMD','/otpVerifyMD/{txn}')
    config.add_route('otpVerifyCus','/otpVerifyCus')
    config.add_route('otpVerifyLogin','/otpVerifyLogin')
    config.add_route('otpVerifyMer','/otpVerifyMer')  
    config.add_route('user','/user')  
    config.add_route('user_voice','/user_voice')  
    config.add_route('merchant','/merchant')  
    config.add_route('userTransaction','/userTransaction')   
    config.add_route('reqTransaction','/reqTransaction')  
    config.add_route('merCredit','/merCredit')  
    config.add_route('merDebit','/merDebit')  
    config.scan('wallet.views')
 
    return config.make_wsgi_app()

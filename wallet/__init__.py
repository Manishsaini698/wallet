from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login','/login')
    config.add_route('signup','/signup')
    config.add_route('createCus','/createCus')
    config.add_route('createMer','/createMer')
    config.add_route('otpLogin','/otpLogin')
    config.add_route('passLogin','/passLogin')
    config.add_route('otpVerify','/otpVerify')  
    config.add_route('user','/user')  
    config.scan('wallet.views')
    return config.make_wsgi_app()

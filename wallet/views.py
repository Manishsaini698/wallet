from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return {'project': 'wallet'}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return {'project': 'wallet'}

@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'project': 'wallet'}

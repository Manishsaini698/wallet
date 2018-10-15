from pyramid.view import view_config
from . import data_service as ds
from . import security

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def home(request):
    return {'project': 'wallet'}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return {'project': 'wallet'}

@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'project': 'wallet'}

class BasicViews:
    def __init__(self, request):
        self.request = request    

    @view_config(route_name='create')
    def create(self):
        request = self.request
        if 'form.submitted' in request.params:
            name = request.params['name']
            email = request.params['email']
            password = request.params['password']                
            mobileno = request.params['mobileno']
            ec = ds.create_customer( name=name, email=email, hashed_password=hash_password(password), mobileno=mobileno)
            request.session.flash("Signup succeeded.")  
        return HTTPFound(location='/')       

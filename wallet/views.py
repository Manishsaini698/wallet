from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from . import data_service as ds
from passlib.hash import bcrypt
from wallet.security import hash_password


        
@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return {'project': 'wallet'}


@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return {'project': 'wallet'}

@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'project': 'wallet'}

@view_config(route_name='otpVerify', renderer='templates/otp.jinja2')
def otpVerify(request):
    return {'project': 'wallet'}

@view_config(route_name='user', renderer='templates/user.jinja2')
def user(request):
    return {'project': 'wallet'}


@view_config(route_name='createCus')
def createCus(request):
    name = request.params['name']
    email = request.params['email']
    password = request.params['password']                
    mobile = request.params['mobileno']   
    ds.create_customer(name=name, email=email, password=password,mobile=mobile )
    return HTTPFound(location='/')

@view_config(route_name='createMer')
def createMer(request):
    name = request.params['name']
    email = request.params['email']
    password = request.params['password']                
    mobile = request.params['mobileno'] 
    address = request.params['address']  
    ds.create_merchant(name=name, email=email, password=password, mobile=mobile, address=address)
    return HTTPFound(location='/')


@view_config(route_name='otpLogin')
def otpLogin(request):
    #mobile = request.params['mobileno']
    ds.sendotp()
    return HTTPFound(location='/otpVerify')


@view_config(route_name='passLogin')
def passLogin(request):
    mobile = request.params['mobileno']
    password = request.params['password']
    return HTTPFound(location='/user')

@view_config(route_name='otpVerify')
def otpVerify(request):
    mobile = request.params['mobileno']
    password = request.params['password']
    return HTTPFound(location='/user')


'''

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
            print('1')
            ec = ds.create_customer( name=name, email=email, hashed_password=hash_password(password), mobileno = mobileno)
            print('2')
            request.session.flash("Signup succeeded.")  
        return HTTPFound(location='/')       

    @view_config(route_name='login')
    def login(self):
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            email = request.params['email']
            password = request.params['password']
            user = check_login(email, password)
            if user is not None :
                headers = remember(request, email)
            message = 'Failed login'
        request.session.flash("Login failed. Please try again.")
        return HTTPFound(location="/")
'''
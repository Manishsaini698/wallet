from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from . import data_service as ds
from passlib.hash import bcrypt
from pyramid.security import forget, remember
from wallet.security import hash_password


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return {'project': 'wallet'}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return {'project':'wallet'}

@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'project': 'wallet'}

@view_config(route_name='enterotp', renderer='templates/otp.jinja2')
def enterotp(request):
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
    mobile = request.params['mobileno']
    remember(request,mobile)
    ds.send_otp(mobile=mobile)
    
    return HTTPFound(location='/enterotp')


@view_config(route_name='passLogin')
def passLogin(request):
    mobile = request.params['mobileno']
    password = request.params['password']
    user = ds.check_login(mobile,password)
    if user is not None:
        remember(request,mobile)
        return HTTPFound(location=request.route_url('user'))
    else:
        return HTTPFound(location=request.route_url('login'))


@view_config(route_name='otpVerify')
def otpVerify(request):
    uid = request.authenticated_userid
    otp = request.params['otp']
    user = ds.otp_verify(mobile=uid,otp=otp)
    if user :
        return HTTPFound(location='/user')



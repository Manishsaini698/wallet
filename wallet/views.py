from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from . import data_service as ds
from passlib.hash import bcrypt
from pyramid.security import forget, remember
from wallet.security import hash_password , check_login


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
    txn = request.matchdict['txn']
    return {'project': 'wallet', 'txn':txn}

@view_config(route_name='user', renderer='templates/user.jinja2')
def user(request):
    uid = request.authenticated_userid
    adict = ds.user_profile_page(uid)
    adict['history'] = ds.trans_his(uid)
    return {'project': 'wallet', **adict}

@view_config(route_name='merchant', renderer='templates/merchant.jinja2')
def merchant(request):
    mid = request.authenticated_userid
    return {'project': 'wallet'}

@view_config(route_name='createCus')
def createCus(request):
    name = request.params['name']
    email = request.params['email']
    password = request.params['password']                
    mobile = request.params['mobileno']
    '''  
    request.session['mobileno'] = mobile 
    request.session['email'] = email    
    request.session['password'] = password    
    request.session['name'] = name 
    '''   
    ds.create_customer(name=name, email=email, hashed_password=hash_password(password),mobile=mobile )
    return HTTPFound(location='/')

@view_config(route_name='createMer')
def createMer(request):
    name = request.params['name']
    email = request.params['email']
    password = request.params['password']                
    mobile = request.params['mobileno'] 
    address = request.params['address']  
    ds.create_merchant(name=name, email=email, hashed_password=hash_password(password), mobile=mobile, address=address)
    return HTTPFound(location='/')


@view_config(route_name='otpLogin')
def otpLogin(request):
    mobile = request.params['mobileno']
    request.session['mobileno'] = mobile
    ds.send_otp(mobile=mobile)
    return HTTPFound(location='/enterotp/')


@view_config(route_name='passLogin')
def passLogin(request):
    mobile = request.params['mobileno']
    password = request.params['password']
    user = check_login(mobile,password)
#    if log.connecter == 'user':
#        user = log.user
    if user is not None:
        headers = remember(request,mobile)
        print(headers)
        return HTTPFound(location=request.route_url('user'),headers=headers)
    else:
        return HTTPFound(location=request.route_url('login'))

'''   if log.connecter == 'mer':
        mer = log.mer
        if mer is not None:
            headers = remember(request,mobile)
            print(headers)
            return HTTPFound(location=request.route_url('mer'),headers=headers)
        else:
            return HTTPFound(location=request.route_url('login'))
'''


@view_config(route_name='otpVerify')
def otpVerify(request):
#    mobile = request.session['mobileno']
#    name = request.session['name']
#    address = request.session['address']
    otp = request.params['otp']
    txn = request.matchdict['txn']
    if txn is not None:
        ds.transact(txn=txn, otp=otp)
        return HTTPFound(location='/user')
'''    elif address is not None:
        ds.create_merchant(name=name, email=email, password=password, mobile=mobile, address=address)
        return HTTPFound(location='/')
    elif name is not None:
        ds.create_customer(name=name, email=email, password=password, mobile=mobile)
        return HTTPFound(location='/')
    else:
        user = ds.otp_verify(mobile=mobile,otp=otp)
        if user is True:
            return HTTPFound(location='/user')

'''
@view_config(route_name='userTransaction')
def userTransaction(request):
    sender = request.authenticated_userid
    reciever = request.params['mobileno']
    payment = request.params['money']
    otp = ds.send_otp(mobile=sender)
    check = ds.check_lock(sender)
    print(check)
    if check is None:
        ds.transaction_lock(sender)
        txn = ds.transaction(sender=sender, reciever=reciever,payment=payment, otp=otp)
        return HTTPFound(location='/enterotp/' + str(txn.id))
    else:
        request.session.flash("can't proceed this transaction")
        return HTTPFound(location='user')


@view_config(route_name='reqTransaction')
def reqTransaction(request):
    reciever = request.authenticated_userid
    sender = request.params['mobileno']
    payment = request.params['money']
    otp = ds.send_otp(mobile=sender)
#    tl_id = ds.transaction_lock(sender=sender)
    txn = ds.transaction(sender=sender, reciever=reciever,payment=payment, otp=otp)
 #   ds.transaction_freelock(sender=sender)
    return HTTPFound(location='/enterotp/' + str(txn.id))
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from . import data_service as ds
from passlib.hash import bcrypt
from pyramid.security import forget, remember
from wallet.security import hash_password , check_login, check_login_mer


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return {'project': 'wallet'}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return {'project':'wallet'}

@view_config(route_name='loginMer', renderer='templates/loginMer.jinja2')
def loginMer(request):
    return {'project':'wallet'}


@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'project': 'wallet'}

@view_config(route_name='enterotp', renderer='templates/otp.jinja2')
def enterotp(request):
    txn = request.matchdict['txn']
    return {'project': 'wallet', 'txn':txn}
    
@view_config(route_name='enterotpM', renderer='templates/otpM.jinja2')
def enterotpM(request):
    txn = request.matchdict['txn']
    return {'project': 'wallet', 'txn':txn}

@view_config(route_name='enterOtpCus', renderer='templates/otpCus.jinja2')
def enterOtpCus(request):
    return {'project': 'wallet'}

@view_config(route_name='enterOtpMer', renderer='templates/otpMer.jinja2')
def enterOtpMer(request):
    return {'project': 'wallet'}

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
    mobile = request.params['mobileno']
    email = request.params['email']
    password = request.params['password']
    name = request.params['name']
    request.session['mobile'] = mobile 
    request.session['email'] = email    
    request.session['password'] = password    
    request.session['name'] = name 
    ds.send_signup_otp(mobile=mobile)
    return HTTPFound(location='/enterOtpCus')

@view_config(route_name='createMer')
def createMer(request):
    mobile = request.params['mobileno']
    email = request.params['email']
    password = request.params['password']
    name = request.params['name']
    address = request.params['address']
    request.session['name'] = name
    request.session['email'] = email 
    request.session['password'] = password                
    request.session['mobile'] = mobile 
    request.session['address'] = address  
    otp = ds.send_signup_otp(mobile=mobile)
    print(otp)
    return HTTPFound(location='/enterOtpMer')


@view_config(route_name='otpLogin')
def otpLogin(request):
    mobile = request.params['mobileno']
    request.session['mobile'] = mobile
    ds.send_otp(mobile=mobile)
    return HTTPFound(location='/enterotp/')


@view_config(route_name='passLogin')
def passLogin(request):
    mobile = request.params['mobileno']
    password = request.params['password']
    user = check_login(mobile,password)
    if user is not None:
        headers = remember(request,mobile)
        print(headers)
        return HTTPFound(location=request.route_url('user'),headers=headers)
    else:
        return HTTPFound(location=request.route_url('login'))


@view_config(route_name='passLoginMer')
def passLoginMer(request):
    mobile = request.params['mobileno']
    password = request.params['password']
    user = check_login_mer(mobile,password)
    print(user)
    if user is not None:
        headers = remember(request,mobile)
        print(headers)
        return HTTPFound(location=request.route_url('merchant'),headers=headers)
    else:
        return HTTPFound(location=request.route_url('loginMer'))


@view_config(route_name='otpVerify')
def otpVerify(request):
    otp = request.params['otp']
    txn = request.matchdict['txn']
    if txn is not None:
        ds.transact(txn=txn, otp=otp)
        return HTTPFound(location='/user')

@view_config(route_name='otpVerifyM')
def otpVerifyM(request):
    otp = request.params['otp']
    txn = request.matchdict['txn']
    if txn is not None:
        ds.transact_mer(txn=txn, otp=otp)
        return HTTPFound(location='/user')

@view_config(route_name='otpVerifyLogin')
def otpVerifyLogin(request):
    mobile = request.session['mobileno']
    otp = request.params['otp']
    user = ds.otp_verify(mobile=mobile,otp=otp)
    if user is True:
        return HTTPFound(location='/user')
            

@view_config(route_name='otpVerifyMer')
def otpVerifyMer(request):
    mobile = request.session['mobile']
    name = request.session['name']
    password = request.session['password']
    email = request.session['email']
    address = request.session['address']
    otp = request.params['otp']
    print(mobile,name,email,address,password)
    verified = ds.otp_verify_signup(mobile=mobile,otp=otp)
    if verified:
        ds.create_merchant(name=name, email=email, hashed_password=hash_password(password), mobile=mobile, address=address)
        return HTTPFound(location='/')

@view_config(route_name='otpVerifyCus')
def otpVerifyCus(request):
    mobile = request.session['mobile']
    name = request.session['name']
    email = request.session['email']
    password = request.session['password']
    otp = request.params['otp']
    verified = ds.otp_verify_signup(mobile=mobile,otp=otp)
    if verified:
        ds.create_customer(name=name, email=email, hashed_password=hash_password(password), mobile=mobile)
    return HTTPFound(location='/')


@view_config(route_name='userTransaction')
def userTransaction(request):
    sender = request.authenticated_userid
    reciever = request.params['mobileno']
    payment = request.params['money']
    otp = ds.send_otp(mobile=sender)
    check = ds.check_lock(sender)
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
    return HTTPFound(location='/enterotpM/' + str(txn.id))

@view_config(route_name='merCredit')
def merCredit(request):
    reciever = request.authenticated_userid
    sender = request.params['mobileno']
    payment = request.params['money']
    otp = ds.send_otp(mobile=sender)
#    tl_id = ds.transaction_lock(sender=sender)
    txn = ds.transaction(sender=sender, reciever=reciever,payment=payment, otp=otp)
 #   ds.transaction_freelock(sender=sender)
    return HTTPFound(location='/enterotpM/' + str(txn.id))

@view_config(route_name='merDebit')
def merDebit(request):
    reciever = request.authenticated_userid
    sender = request.params['mobileno']
    payment = request.params['money']
    otp = ds.send_otp(mobile=sender)
#    tl_id = ds.transaction_lock(sender=sender)
    txn = ds.transaction(sender=sender, reciever=reciever,payment=payment, otp=otp)
 #   ds.transaction_freelock(sender=sender)
    return HTTPFound(location='/enterotp/' + str(txn.id))
     

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    url = request.route_url('home')
    request.session.flash("You have logged out successfully.")        
    return HTTPFound(location=url,headers=headers) 
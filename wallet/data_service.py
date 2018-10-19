from mongoengine import connect
from . import models
import pyotp
from wallet.emailing import send_email

connect('wallet')

def create_customer(**kwargs):
    customer = models.Customer()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobile = kwargs['mobile']
    customer.password = kwargs['password']
    customer.save()
    print('yoyo')

def create_merchant(**kwargs):
    customer = models.Merchant()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobileno = kwargs['mobileno']
    customer.hashed_pass = kwargs['hashed_password']
    customer.cid = ''.join(customer.name.split(' ')).lower()
    customer.save()

def check_login(mobile, password):
    user = models.Customer.objects(mobile=mobile).first()
    passw = user.password
    
    if user and passw == password:
        print(user)
        return user
    else :
        return None

def send_otp(**kwargs):
    totp = pyotp.TOTP('base32secret3232')
    message = totp.now()
    mobile = kwargs['mobile']
    user = models.Customer.objects(mobile=mobile).first()
    user.login_otp = message
    user.save()
    send_email('manish1216237@jmit.ac.in',message)

def otp_verify(**kwargs):
    mobile = kwargs['mobile']
    user = models.Customer.objects(mobile=mobile).first()
    if user.login_otp == kwargs['otp']:
        return True
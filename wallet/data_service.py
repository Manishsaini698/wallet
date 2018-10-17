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
    company = models.Merchant()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobileno = kwargs['mobileno']
    customer.hashed_pass = kwargs['hashed_password']
    customer.cid = ''.join(customer.name.split(' ')).lower()
    customer.save()

def sendotp(**kwargs):
    totp = pyotp.TOTP('base32secret3232')
    message = totp.now()
    send_email('manish1216237@jmit.ac.in',message)

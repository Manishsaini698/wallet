from mongoengine import connect
from . import models

connect('wallet')


def create_customer(**kwargs):
    company = models.Startup()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobileno = kwargs['mobileno']
    customer.hashed_pass = kwargs['hashed_password']
    customer.cid = ''.join(customer.name.split(' ')).lower()
    customer.save()
    print('yoyo')


from mongoengine import connect
from . import models

connect('wallet')

def create_customer(**kwargs):
    customer = models.Customer()
    customer.name = kwargs['name'].capitalize()
    customer.mobile_no = kwargs[int('mobile_no')]
    #customer.hashed_pass = kwargs['hashed_password']
    customer.save()

from mongoengine import connect
from . import models
import pyotp
from wallet.emailing import send_email
import bcrypt
import datetime


connect('wallet')

def get_for_auth(mobile):
        return models.Customer.objects(mobile=mobile).first()

def create_customer(**kwargs):
    customer = models.Customer()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobile = kwargs['mobile']
    customer.hashed_password = kwargs['password']    
    customer.save()

def create_merchant(**kwargs):
    customer = models.Merchant()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobileno = kwargs['mobileno']
    customer.hashed_pass = kwargs['hashed_password']
    customer.cid = ''.join(customer.name.split(' ')).lower()
    customer.save()


def send_otp(**kwargs):
    totp = pyotp.TOTP('base32secret3232')
    message = totp.now()
    mobile = kwargs['mobile']
    user = models.Customer.objects(mobile=mobile).first()
    user.login_otp = message
    user.save()
    send_email('manish1216237@jmit.ac.in',message)
    return message

def otp_verify(**kwargs):
    mobile = kwargs['mobile']
    user = models.Customer.objects(mobile=mobile).first()
    if user.login_otp == kwargs['otp']:
        return True


def user_profile_page(mobile):
    user = models.Customer.objects(mobile=mobile).first()
    return {'wallet_bal':user.wallet_bal}

def transaction(**kwargs):
    transaction = models.Transaction()
    transaction.trans_from = kwargs['sender'] 
    transaction.trans_to = kwargs['reciever']
    transaction.trans_value = kwargs['payment']
    print(kwargs['otp'])
    transaction.trans_otp = kwargs['otp']
    return transaction.save() 
            
def transact(**kwargs):
    tid = kwargs['txn']
    otp = kwargs['otp']  
    transc = models.Transaction.objects(id=tid).first()
    if transc.trans_otp == otp:
        sender = models.Customer.objects(mobile=transc.trans_from).first()
        sender.wallet_bal = sender.wallet_bal - transc.trans_value
        sender.trans_history.append(transc.id)
        reciever = models.Customer.objects(mobile=transc.trans_to).first()
        reciever.wallet_bal =reciever.wallet_bal + transc.trans_value
        transc.trans_status = True    
        sender.save()
        reciever.save()
        transc.save()

def trans_his(uid):
    user = models.Customer.objects(mobile=uid).first()
    txns = user.trans_history
    return_this = []
    for txn in txns:
        trans = models.Transaction.objects(id=txn).first()    
        a = {}
        a['to'] = trans.trans_to
        a['from'] = trans.trans_from
        a['value'] = trans.trans_value
        a['date'] = trans.trans_time
        return_this.append(a)
    print(return_this)
    return return_this
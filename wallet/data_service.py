from mongoengine import connect
from . import models
import pyotp
from wallet.emailing import send_email
import bcrypt
import datetime


connect('wallet')

def get_for_auth_user(mobile):
        return models.Customer.objects(mobile=mobile).first()

def get_for_auth_mer(mobile):
        return models.Merchant.objects(mobile=mobile).first()

def create_customer(**kwargs):
    customer = models.Customer()
    customer.email = kwargs['email']
    customer.name = kwargs['name'].capitalize()
    customer.mobile = kwargs['mobile']
    customer.hashed_password = kwargs['hashed_password']
    customer.save()

def create_merchant(**kwargs):
    merchant = models.Merchant()
    merchant.email = kwargs['email']
    merchant.name = kwargs['name'].capitalize()
    merchant.mobile = kwargs['mobile']
    merchant.address = kwargs['address']
    merchant.hashed_password = kwargs['hashed_password']
    merchant.save()

def send_login_otp(**kwargs):
    totp = pyotp.TOTP('base32secret3232')
    message = totp.now()
    mobile = kwargs['mobile']
    user = models.Otp()
    user.mobile = mobile
    user.login_otp = message
    user.save()
    send_email('manish1216237@jmit.ac.in',message)
    return message

def send_signup_otp(**kwargs):
    totp = pyotp.TOTP('base32secret3232')
    message = totp.now()
    mobile = kwargs['mobile']
    user = models.Otp()
    user.mobile = mobile
    user.signup_otp = message
    user.save()
    send_email('manish1216237@jmit.ac.in',message)
    return message


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


def otp_verify_signup(**kwargs):
    mobile = kwargs['mobile']
    user = models.Otp.objects(mobile=mobile).first()
    if user.signup_otp == kwargs['otp']:
        return True


def user_profile_page(mobile):
    user = models.Customer.objects(mobile=mobile).first()
    return {'wallet_bal':user.wallet_bal}

def transaction(**kwargs):
    transaction = models.Transaction()
    transaction.trans_from = kwargs['sender'] 
    transaction.trans_to = kwargs['reciever']
    transaction.trans_value = kwargs['payment']
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
        transaction_freelock(transc.trans_from)
            
def transact_mer(**kwargs):
    tid = kwargs['txn']
    otp = kwargs['otp']  
    transc = models.Transaction.objects(id=tid).first()
    if transc.trans_otp == otp:
        sender = models.Merchant.objects(mobile=transc.trans_from).first()
        sender.wallet_bal = sender.wallet_bal - transc.trans_value
        sender.trans_history.append(transc.id)
        reciever = models.Customer.objects(mobile=transc.trans_to).first()
        reciever.wallet_bal =reciever.wallet_bal + transc.trans_value
        transc.trans_status = True    
        sender.save()
        reciever.save()
        transc.save()
        transaction_freelock(transc.trans_from)

def transact_merD(**kwargs):
    tid = kwargs['txn']
    otp = kwargs['otp']  
    transc = models.Transaction.objects(id=tid).first()
    if transc.trans_otp == otp:
        sender = models.Customer.objects(mobile=transc.trans_from).first()
        sender.wallet_bal = sender.wallet_bal - transc.trans_value
        sender.trans_history.append(transc.id)
        reciever = models.Merchant.objects(mobile=transc.trans_to).first()
        reciever.wallet_bal =reciever.wallet_bal + transc.trans_value
        transc.trans_status = True    
        sender.save()
        reciever.save()
        transc.save()
        transaction_freelock(transc.trans_from)

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
    return return_this

def check_lock(sender):
    user = models.TransactionLock.objects(trans_sender=sender)
    print(user)
    if user == []:
        return False
    else: 
        True

def transaction_lock(sender):
    trans = models.TransactionLock()
    trans.trans_sender = sender
    trans.save()

def transaction_freelock(sender):
    models.TransactionLock.objects(trans_sender=sender).first().delete()

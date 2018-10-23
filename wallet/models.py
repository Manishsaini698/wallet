import mongoengine
import datetime


class Otp(mongoengine.Document):
        mobile = mongoengine.StringField()
        login_otp = mongoengine.StringField()
        signup_otp = mongoengine.StringField()
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        hashed_password = mongoengine.StringField()        

class Customer(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        hashed_password = mongoengine.StringField()       
        mobile = mongoengine.StringField() 
        login_otp = mongoengine.StringField()
        wallet_bal = mongoengine.DecimalField(default=0.0)
        trans_history = mongoengine.ListField(mongoengine.ObjectIdField())

class Merchant(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        hashed_password = mongoengine.StringField()       
        mobile = mongoengine.StringField()   
        address = mongoengine.StringField()
        login_otp = mongoengine.StringField()
        verified = mongoengine.StringField() 

class Transaction(mongoengine.Document):
        trans_to = mongoengine.StringField()
        trans_from = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 
        trans_time = mongoengine.DateTimeField(default=datetime.datetime.now())
        trans_status = mongoengine.BooleanField(default=False)
        trans_value = mongoengine.DecimalField()
        trans_lock_id = mongoengine.ObjectIdField()

class TransactionLock(mongoengine.Document):
        trans_sender = mongoengine.StringField()
        
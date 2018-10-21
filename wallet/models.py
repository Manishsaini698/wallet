import mongoengine
import datetime

class Customer(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        hashed_password = mongoengine.StringField()       
        mobile = mongoengine.StringField() 
        login_otp = mongoengine.StringField()
        wallet_bal = mongoengine.DecimalField()
        trans_history = mongoengine.ListField(mongoengine.ObjectIdField())

class Merchant(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        hashed_password = mongoengine.StringField()       
        mobile = mongoengine.StringField()   
        address = mongoengine.StringField()
        login_otp = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 
        verified = mongoengine.StringField() 

class Transaction(mongoengine.Document):
        trans_to = mongoengine.StringField()
        trans_from = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 
        trans_time = mongoengine.DateTimeField(default=datetime.datetime.now())
        trans_status = mongoengine.BooleanField(default=False)
        trans_value = mongoengine.DecimalField()

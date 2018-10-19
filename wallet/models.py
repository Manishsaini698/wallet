import mongoengine

class Customer(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        password = mongoengine.StringField()       
        mobile = mongoengine.StringField() 
        login_otp = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 
        trans_time = mongoengine.DateTimeField()
        wallet_bal = mongoengine.StringField()
        trans_history = mongoengine.ListField()


     
class Merchant(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.EmailField()        
        password = mongoengine.StringField()       
        mobile = mongoengine.StringField()   
        address = mongoengine.StringField()
        login_otp = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 
        verified = mongoengine.StringField() 


import mongoengine

class Customer(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.StringField()        
        password = mongoengine.StringField()       
        mobile = mongoengine.StringField() 
        login_otp = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 

     
class Merchant(mongoengine.Document):
        name = mongoengine.StringField()
        email = mongoengine.StringField()        
        password = mongoengine.StringField()       
        mobile = mongoengine.StringField()   
        address = mongoengine.StringField()
        login_otp = mongoengine.StringField()
        trans_otp = mongoengine.StringField() 
        verified = mongoengine.StringField() 


import mongoengine

class Customer(mongoengine.Document):
        name = mongoengine.StringField(min_length=5, max_length=30, required=True, unique=True)
        hashed_pass = mongoengine.StringField(min_length=5, required=True)
        mobile_no = mongoengine.StringField(required=True)
        login_otp = mongoengine.StringField(required=True)
        trans_otp = mongoengine.StringField(required=True)

from passlib.hash import bcrypt
from . import data_service as ds

def check_login(email, password):
    user = ds.get_for_auth(email)
    if user and bcrypt.verify(password, user.hashed_pass):
        return user
    else :
        return None
       

def hash_password(pasie):
    return bcrypt.hash(pasie)
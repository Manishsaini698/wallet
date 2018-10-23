from passlib.hash import bcrypt
from . import data_service as ds
import bcrypt


def check_login(mobile, password):
    user = ds.get_for_auth_user(mobile)
#    mer = ds.get_for_auth_mer(mobile)
    if user is not None and check_password(password, user.hashed_password):
        return user
#    elif mer is not None and check_password(password, mer.hashed_password):
#        return {'connecter':'mer','mer':mer}
    else:
        None
       

def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    return pwhash.decode('utf-8')

def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf-8')
    return bcrypt.checkpw(pw.encode('utf-8'), expected_hash)

def groupfinder(userid, request):
            return ['group:users']

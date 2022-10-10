import hashlib
import Master_Password
import uuid

def isPassword(input_master_password):
    salt=str(uuid.uuid4())
    input_master_password+=salt
    master_password=Master_Password.mass_pwd()
    master_password+=salt
    if hashlib.md5(master_password.encode()).hexdigest()==hashlib.md5(input_master_password.encode()).hexdigest():
        return True
    else:
        return False
pass

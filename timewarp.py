import secrets
import string
import hashlib

# recieved a lot of insperation/help from https://www.pythoncentral.io/hashing-strings-with-python/

def generate_key():
    key = b'gamekey__012345pst'

    letters = string.ascii_letters
    salt = ''.join(secrets.choice(letters) for i in range(100))

    
    hashed_key = hashlib.sha256(salt[::-1].encode() + key).hexdigest() + ':' + salt
    return hashed_key

def validate_key(hashed_key):
    key = b'gamekey__012345pst'

    given_key, salt = hashed_key.split(':')
    if given_key == hashlib.sha256(salt[::-1].encode() + key).hexdigest():
        return True
    else:
        return False
    


print(validate_key(generate_key()))
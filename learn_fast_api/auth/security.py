from passlib.context import CryptContext

_passwordContext = CryptContext(schemes=['bcrypt'], deprecated='auto')


# hashing the user password before saving it in DB
def hash(password: str):
    return _passwordContext.hash(password)


# returning a bool if the password is verified to the user hashed password
def verify(password: str, hashedPassword: str):
    return _passwordContext.verify(password, hashedPassword)

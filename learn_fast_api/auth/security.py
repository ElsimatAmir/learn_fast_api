from passlib.context import CryptContext

_passwordContext = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash(password: str):
    return _passwordContext.hash(password)

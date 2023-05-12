import jwt
import time
from core.secretData import secretData


tokenSecret = secretData["SECRET_KEY"]
algorithm = secretData["ALGORITHM"]


def _tokenResponse(token: str):
    return {
        "access token": token
    }


def _decodeToken(token: str):
    try:
        decodedToken = jwt.decode(token, tokenSecret, algorithms=algorithm)
        return decodedToken if decodedToken['expires'] >= time.time() else None
    except:
        return


def signToken(userID: int):
    payload = {
        "userID": userID,
        "expires": time.time() + 1200
    }
    token = jwt.decode(payload, tokenSecret, algorithms=algorithm)
    return _tokenResponse(token=token)

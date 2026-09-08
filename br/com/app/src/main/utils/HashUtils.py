from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from argon2.exceptions import VerificationError
from argon2.exceptions import InvalidHashError
from domain.exceptions.UnauthorizedException import UnauthorizedException

class HashUtils:

  def __init__(self):
    self.ph = PasswordHasher()

  def gen_hash(self, text):
    return self.ph.hash(text)

  def verify_hash(self, text, hash_text):
    try:
      return self.ph.verify(hash_text, text)
    except VerifyMismatchError:
      raise UnauthorizedException()
    except InvalidHashError:
      raise UnauthorizedException()
    except VerificationError: 
      raise UnauthorizedException()


from argon2 import PasswordHasher

class HashUtils:

  def __init__(self):
    self.ph = PasswordHasher()

  def gen_hash(self, text):
    return self.ph.hash(text)

  def verify_hash(self, text, hash_text):
    return self.ph.verify(text, hash_text)
    

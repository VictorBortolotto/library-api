from dataclasses import dataclass

@dataclass
class UserLoginRequest:
  id: int
  email: str
  password: str
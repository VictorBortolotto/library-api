from dataclasses import dataclass

@dataclass
class UserLoginRequest:
  id: int
  is_valid_login: bool
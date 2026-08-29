from dataclasses import dataclass

@dataclass
class CreateClientDto:
  user_id: str
  name: str
  phone: str
  address: str
  zip_code: str
  city: str
  neighborhood: str
  country: str
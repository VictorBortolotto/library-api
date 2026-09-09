import requests
from flask import jsonify
from domain.exceptions.NotFoundException import NotFoundException
from domain.dto.viacep.ViaCepDataDto import ViaCepDataDto

class ExternalApiService:

  def find_by_cep(self, cep):

    response = requests.get(
      f"https://viacep.com.br/ws/{cep}/json/"
    )

    response.raise_for_status()

    viaCep = response.json()

    if viaCep is None:
      raise NotFoundException()
    
    return ViaCepDataDto(
      viaCep['cep'],
      viaCep['logradouro'],
      viaCep['complemento'],
      viaCep['unidade'],
      viaCep['bairro'],
      viaCep['localidade'],
      viaCep['uf'],
      viaCep['estado'],
      viaCep['regiao'],
      viaCep['ibge'],
      viaCep['gia'],
      viaCep['ddd'],
      viaCep['siafi']
    )
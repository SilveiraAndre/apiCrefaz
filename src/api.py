import requests
import json

class ApiCrefaz:
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.token = None

    def login(self):
        
        url = "https://api-externo.crefazon.com.br/api/Usuario/login"
        payload = json.dumps({"login": "CC030165094","senha": "060893","apiKey": self.api_key})
        headers = {'Accept': 'application/json','Content-Type': 'application/json'}

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            response_data = response.json()
            self.token = response_data['data']['token']
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.RequestException as err:
            print(err)
            self.token = None

    def cadastrar_proposta(self, payload):
        if not self.token:
            print("Token inválido.")
            return
        url = "https://api-externo.crefazon.com.br/api/Proposta"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            response_data = response.json()
            nome = payload['nome']
            cpf = payload['cpf']
            return nome, cpf, response_data['data']['propostaId'], response_data['data']['aprovado']
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: ApiCrefaz>cadastrar_proposta{e}")
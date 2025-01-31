from database import Database
from api import ApiCrefaz
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

driver = os.getenv('driver')
server = os.getenv('server')
database = os.getenv('database')
uid = os.getenv('uid')
pwd = os.getenv('pwd')
api_key = os.getenv('api_key')

# instancias 
database = Database(driver, server, database, uid, pwd)
api = ApiCrefaz(api_key)

# conn 
database.connect()
df = database.query("SELECT * FROM TB_MIS_CADASTRO_PROPOSTA_CREFAZ")
# print(df)

# login
api.login()
proposta_payload = {
    "nome": df['NM_NOME'].iloc[0],
    "cpf": str(df['NU_CPF_CNPJ'].iloc[0]),
    "nascimento": df['DT_NASCIMENTO'].iloc[0],
    "telefone": df['TEL'].iloc[0],
    "ocupacaoId": 1,
    "cep": "63030000",
    "cidadeId": 1762,
    "bairro": "Bairro",
    "logradouro": "Nome da Rua",
    "urlNotificacaoParceiro": "https://URL_DE_NOTIFICACAO"
}
response = api.cadastrar_proposta(proposta_payload)
print(response)
# print(proposta_payload)

df1 = database.update_value(response[2], response[3], response[1])

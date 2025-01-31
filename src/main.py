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
print(df)

# login
api.login()

for _, row in df.iterrows():
    proposta_payload = database.create_payload(row)
    print('payload ok')
    print(proposta_payload)
    response = api.cadastrar_proposta(proposta_payload)
    print('cadastrar proposta ok')

    if response:
        print(response)
        id_cliente = row['ID_CLIENTE']
        database.update_value(response[2], response[3], response[1], id_cliente)


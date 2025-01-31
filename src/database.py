import pyodbc
import pandas as pd
import datetime

class Database:
    def __init__(self, driver, server, database, uid, pwd):
        self.driver = driver
        self.server = server
        self.database = database
        self.uid = uid
        self.pwd = pwd
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            string_conn = f"DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.uid};PWD={self.pwd}"
            self.conn = pyodbc.connect(string_conn)
            self.cursor = self.conn.cursor()
            print('successfull connection')
        except Exception as e:
            print(e)

    def query(self, query):
        if self.conn:
            return pd.read_sql(query, self.conn)
            
        else:
            print("erro query")

    def update_value(self, idProposta, status, cpf, id_cliente):
        curdatetime = datetime.datetime.now()
        print(curdatetime.strftime("%d%m%Y %H%M%S"))
        update_query = f"""update TB_MIS_CADASTRO_PROPOSTA_CREFAZ set id_proposta = '{idProposta}', STATUS = '{status}', DATA_PROPOSTA = '{curdatetime.strftime("%d-%m-%Y %H:%M:%S")}' where NU_CPF_CNPJ = '{cpf}'"""
        insert_query_id_proposta = f"insert into tb_cliente_detalhe values ('{id_cliente}',1049,'{idProposta}')"
        insert_query_status_proposta = f"insert into tb_cliente_detalhe values ('{id_cliente}',1050,'{status}')"
        try:
            self.cursor.execute(update_query)
            self.conn.commit()
            self.cursor.execute(insert_query_id_proposta)
            self.conn.commit()
            self.cursor.execute(insert_query_status_proposta)
            self.conn.commit()
            print('successfull update')
        except Exception as e:
            print(e)

    def create_payload(self, row):
        return {
        "nome": row['NM_NOME'],
        "cpf": str(row['NU_CPF_CNPJ']),
        "nascimento": row['DT_NASCIMENTO'],
        "telefone": row['TEL'],
        "ocupacaoId": 1,
        "cep": "63030000",
        "cidadeId": 1762,
        "bairro": "Bairro",
        "logradouro": "Nome da Rua",
        "urlNotificacaoParceiro": "https://URL_DE_NOTIFICACAO"
        }
    
        
        
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
        except Exception as e:
            print(e)

    def query(self, query):
        if self.conn:
            return pd.read_sql(query, self.conn)
        else:
            print("erro query")

    def update_value(self, idProposta, status, cpf):
        curdatetime = datetime.datetime.now()
        print(curdatetime.strftime("%d%m%Y %H%M%S"))
        update_query = f"""update TB_MIS_CADASTRO_PROPOSTA_CREFAZ set id_proposta = '{idProposta}', STATUS = '{status}', DATA_PROPOSTA = '{curdatetime.strftime("%d-%m-%Y %H:%M:%S")}' where NU_CPF_CNPJ = '{cpf}'"""
        try:
            self.cursor.execute(update_query)
            self.conn.commit()
            print('successfull update')
        except Exception as e:
            print(e)
        
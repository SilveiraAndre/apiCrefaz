





	select * from tb_cliente
	where id_cliente = 14460665


select top 10 * from tb_cliente
where ID_CEDENTE = 74
and NM_NOME like '%lourdes%'
and id_cliente = 13725338
order by 1


where id_cliente = 14460665

select * from TB_CLIENTE_TELEFONE
--where id_cliente = 1446013725338665
--where id_cliente = 13725338
where id_cliente = 13725339


    # payload = {
    #     "nome": "J�lio Rossato",
    #     "cpf": "15119796826",
    #     "nascimento": "1980-05-03",
    #     "telefone": "44999167734",
    #     "ocupacaoId": 1,
    #     "cep": "63030000",
    #     "cidadeId": 1762,
    #     "bairro": "Bairro",
    #     "logradouro": "Nome da Rua",
    #     "urlNotificacaoParceiro": "https://URL_DE_NOTIFICACAO"
    # }

    payload = {
        "nome": "VALTER APARECIDO OLIVEIRA DOS REIS",
        "cpf": "28196027893",
        "nascimento": "1978-03-23",
        "telefone": "14996321282",
        "ocupacaoId": 1,
        "cep": "63030000",
        "cidadeId": 1762,
        "bairro": "Bairro",
        "logradouro": "Nome da Rua",
        "urlNotificacaoParceiro": "https://URL_DE_NOTIFICACAO"
    }

Nome: J�lio Rossato, Cpf: 15119796826, IdProposta: 1036223275, Status: True
Nome: VALTER APARECIDO OLIVEIRA DOS REIS, Cpf: 28196027893, IdProposta: 1036223476, Status: False

DROP TABLE TB_MIS_CADASTRO_PROPOSTA_CREFAZ

CREATE TABLE TB_MIS_CADASTRO_PROPOSTA_CREFAZ (
ID_CLIENTE INT NULL, 
NU_CPF_CNPJ VARCHAR(25) NULL, 
NM_NOME VARCHAR(255) NULL, 
TEL VARCHAR(25) NULL, 
DT_NASCIMENTO DATE NULL,
ID_PROPOSTA VARCHAR(75) NULL,
STATUS VARCHAR(75) NULL,
DATA_PROPOSTA SMALLDATETIME,
CAMPO1 VARCHAR(MAX) NULL,
CAMPO2 VARCHAR(MAX) NULL
)

--select top 5
--	  VC.ID_CLIENTE
--	, VC.NU_CPF_CNPJ
--	, VC.NM_NOME
--	, TEL = CONCAT(NU_DDD,NU_TELEFONE)
--	, DT_NASCIMENTO = CASE WHEN DT_NASCIMENTO IS NULL THEN CAST(NULL AS DATE) ELSE CAST(DT_NASCIMENTO AS DATE) END
--	, ID_PROPOSTA = CAST(NULL AS VARCHAR)
--	, STATUS = CAST(NULL AS VARCHAR)
--	, DATA_PROPOSTA = CAST(NULL AS DATETIME)
--	, CAMPO1 = CAST(NULL AS VARCHAR)
--	, CAMPO2 = CAST(NULL AS VARCHAR)
--INTO TB_MIS_CADASTRO_PROPOSTA_CREFAZ
--from tb_visao_carteira_crefaz VC
--JOIN TB_CLIENTE_TELEFONE CT ON VC.ID_CLIENTE = CT.ID_CLIENTE 
--JOIN TB_CLIENTE C ON VC.ID_CLIENTE = C.ID_CLIENTE
--WHERE C.ID_CEDENTE = 74
--ORDER BY VC.NM_NOME


--TRUNCATE TABLE TB_MIS_CADASTRO_PROPOSTA_CREFAZ

insert into TB_MIS_CADASTRO_PROPOSTA_CREFAZ
select TOP 1 
ID_CLIENTE = 1,
NU_CPF_CNPJ = '15119796826',
NM_NOME = 'J�lio Rossato',
TEL = '44999167734',
DT_NASCIMENTO = '1980-05-03',
ID_PROPOSTA = NULL,
STATUS = NULL,
DATA_PROPOSTA = NULL,
CAMPO1 = NULL,
CAMPO2 = NULL 

insert into TB_MIS_CADASTRO_PROPOSTA_CREFAZ
select TOP 1 
ID_CLIENTE = 2,
NU_CPF_CNPJ = '28196027893',
NM_NOME = 'VALTER APARECIDO OLIVEIRA DOS REIS',
TEL = '14996321282',
DT_NASCIMENTO = '1978-03-23',
ID_PROPOSTA = NULL,
STATUS = NULL,
DATA_PROPOSTA = NULL,
CAMPO1 = NULL,
CAMPO2 = NULL 

--DELETE FROM TB_MIS_CADASTRO_PROPOSTA_CREFAZ 
--WHERE ID_CLIENTE NOT IN (1,2)

SELECT * FROM TB_MIS_CADASTRO_PROPOSTA_CREFAZ 

update TB_MIS_CADASTRO_PROPOSTA_CREFAZ 
set id_proposta = null, STATUS = null, DATA_PROPOSTA = null

print getdate()
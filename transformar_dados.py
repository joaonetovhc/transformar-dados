import pandas as pd
import tabula
import zipfile

def extrair_pdf(dir_pdf):
    tabelas = tabula.read_pdf(dir_pdf, pages='3-181')

    dataframe = pd.DataFrame()
    for tabela in tabelas:
        df = tabela.copy()
        dataframe = pd.concat([dataframe, df], ignore_index=True)

    return dataframe   

dir_pdf = 'dados/anexo1.pdf'
dataframe = extrair_pdf(dir_pdf)


# alterando o nome das colunas
dataframe.columns = [col.replace("OD", "SEG. ODONTOLÓGICA") for col in dataframe.columns]
dataframe.columns = [col.replace("AMB", "SEG. AMBULATORIAL") for col in dataframe.columns]

# caso queira salvar em Excel
# dataframe.to_excel('dados/dados_anexo.xlsx', index=False) 

# salvar em CSV
dataframe.to_csv('dados/dados_anexo.csv', index=False, encoding='utf-8', sep=';')

#Teste_Joao_Neto.zip

dir_zip = 'dados/Teste_Joao_Neto.zip'
with zipfile.ZipFile(dir_zip, 'w') as zipf:
    zipf.write('dados/dados_anexo.csv')
print(f"Arquivo ZIP {dir_zip} criado.")
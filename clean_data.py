import pandas as pd
from unicodedata import normalize
from datetime import datetime


# formatando o nomedas colunas
def to_clean_data(data):

    def format_column_names(text):
        
        string_step1 = text.replace(".", "_")
        string_step2 = string_step1.replace(' ', "_")
        string_step3 = string_step2.replace('/', '_')
        string_step4 = string_step3.replace('__', '_')
    
        if '_' == string_step4[-1]:
            return normalize('NFKD', string_step4[:-1]).encode('ASCII', 'ignore').decode('ASCII')
        else:
            return normalize('NFKD', string_step4).encode('ASCII', 'ignore').decode('ASCII')
    

    
    # retirando o caracter "." dos valores
    columns_decimal = ['P/VP','Liquidez', 'Cotação', 'Valor de Mercado', 'Preço do m2','Aluguel por m2']
    
    for column in columns_decimal:
        data[column] = data[column].str.replace(".", "")
    
    # trocando o caracter "," por "." e transformando o valor para float
    
    for column in columns_decimal:
        data[column] = data[column].str.replace(",", ".").astype(float)

    # Retirando o Caracter "%" das colunas

    columns_to_clean = ['Dividend Yield', 'FFO Yield', 'Vacância Média', 'Cap Rate']
    
    for column in columns_to_clean:
        data[column] = data[column].str.replace("%","")
    
    # Retirando os caracterer "."
    
    for column in columns_to_clean:
        data.loc[data[column].str.len() >= 6, column] = data[column].str.replace(".", "")
    
    # transformando os valores para float
    
    for column in columns_to_clean:
        data[column] = data[column].str.replace(",", ".").astype(float)
    
    # transformando a porcentagem na forma decimal
    
    data['Dividend Yield'] = data['Dividend Yield']/100
    data['FFO Yield'] = data['FFO Yield']/100
    data['Vacância Média'] = data['Vacância Média']/100
    data['Cap Rate'] = data['Cap Rate']/100

    columns = list(data.columns)
    new_columns = {col: format_column_names(col.upper()) for col in columns}
    data.rename(columns=new_columns, inplace=True)
    
    return data

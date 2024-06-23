import requests
import pandas as pd

# https://interativos.ge.globo.com/futebol/rotatividade-dos-tecnicos
# URL da API
url = "https://api.gcn.ge.globo.com/api/rotatividade-dos-tecnicos/vinculos/clubes?page=1&per_page=50000"

# Fazendo a requisição HTTP para obter os dados
response = requests.get(url)
data = response.json()

# Extraindo os dados das equipes
equipes = data['equipes']

# Inicializando uma lista para armazenar os dados
vinculos = []

# Percorrendo cada equipe e seus vínculos
for equipe in equipes:
    clube_info = equipe['equipe']
    nome_clube = clube_info['nome_popular']
    estado = clube_info['estado']
    
    for vinculo in equipe['vinculos']:
        tecnico_info = vinculo['tecnico']
        nome_tecnico = tecnico_info['nome_popular']
        nacionalidade_tecnico = tecnico_info['nacionalidade']
        
        tipo_vinculo = vinculo['tipo_vinculo']
        estreia = vinculo['estreia']
        data_inicio = vinculo['data_inicio']
        data_fim = vinculo['data_fim']
        vitorias = vinculo['vitorias']
        empates = vinculo['empates']
        derrotas = vinculo['derrotas']
        tipo_transacao_entrada = vinculo['tipo_transacao_entrada']
        tipo_transacao_saida = vinculo['tipo_transacao_saida']
        eventos = vinculo['eventos']
        
        # Adicionando os dados à lista
        vinculos.append([
            nome_clube, estado, nome_tecnico, nacionalidade_tecnico, 
            tipo_vinculo, estreia, data_inicio, data_fim, 
            vitorias, empates, derrotas, 
            tipo_transacao_entrada, tipo_transacao_saida, eventos
        ])

# Convertendo a lista para um dataframe do pandas
df_vinculos = pd.DataFrame(vinculos, columns=[
    'Nome do Clube', 'Estado', 
    'Nome do Técnico', 'Nacionalidade do Técnico', 
    'Tipo de Vínculo', 'Estreia', 'Data Início', 'Data Fim', 
    'Vitórias', 'Empates', 'Derrotas', 
    'Tipo Transação Entrada', 'Tipo Transação Saída', 'Eventos'
])

# Exibindo a tabela
# print("Tabela de Vínculos")
# print(df_vinculos)

# Opcional: Salvar o dataframe em um arquivo CSV para análise posterior
df_vinculos.to_csv('vinculos_tecnicos_clubes.csv', index=False)

df_vinculos

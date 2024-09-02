import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import time
links = [
    #Dentro dessa lista a gente coloca os links para download direto
]
# Local onde os arquivos serão salvos
pasta_destino = 'C:/Users/borges/Documents/PythonPDF'

os.makedirs(pasta_destino, exist_ok=True) #verifico se a pasta exista

resultados = [] #crio uma lista pra armazenar os resultados

for link in links:
    nome_arquivo = link.split('/')[-1]
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    try:
        inicio = time.time()
        resposta = requests.get(link)
        resposta.raise_for_status()  # Levanta um erro para status de resposta não OK
        fim = time.time()

        with open(caminho_arquivo, 'wb') as f:
            f.write(resposta.content)

        duracao = fim - inicio
        resultados.append([link, 'Sucesso', duracao])
        print(f'Download concluído: {nome_arquivo} em {duracao:.2f} segundos')

    except requests.exceptions.RequestException as e:
        resultados.append([link, f'Falha: {str(e)}', None])
        print(f'Erro ao baixar: {nome_arquivo} - {e}')

#crio a planilha com 3 colunas para uma avaliação posterior
df = pd.DataFrame(resultados, columns=['Link de Download', 'Status', 'Tempo de Download'])

#salvo as informações na planilha
caminho_excel = os.path.join(pasta_destino, 'resultados_downloads.xlsx')
df.to_excel(caminho_excel, index=False)

print("Planilha salva com sucesso!")

# ### Trecho do código onde configuramos o PLOTLY ###

df = pd.read_excel(caminho_excel)

contagem_status = df['Status'].value_counts().reset_index()
contagem_status.columns = ['Status', 'Quantidade']

df_falhas = df[df['Status'].str.startswith('Falha')]
contagem_erros = df_falhas['Status'].value_counts().reset_index()
contagem_erros.columns = ['Erro', 'Quantidade']

df_sucesso = df[df['Status'] == 'Sucesso']
tempo_medio = df_sucesso['Tempo de Download'].mean()

fig1 = px.bar(contagem_status, x='Status', y='Quantidade',
              title='Distribuição de Sucessos e Falhas nos Downloads',
              color='Status',
              text='Quantidade')

fig1.update_traces(texttemplate='%{text}', textposition='outside')
fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig1.show()


if not contagem_erros.empty:
    fig2 = px.pie(contagem_erros, names='Erro', values='Quantidade',
                 title='Tipos de Erros nos Downloads',
                 hole=0.3)
    fig2.show()
else:
    print("Nenhum erro registrado para exibir no gráfico de erros.")

if not df_sucesso.empty:
    fig3 = px.histogram(df_sucesso, x='Tempo de Download',
                        nbins=10,
                        title='Distribuição do Tempo de Download',
                        labels={'Tempo de Download': 'Tempo (segundos)'},
                        opacity=0.75)
    fig3.add_vline(x=tempo_medio, line_dash="dash", line_color="red",
                  annotation_text=f'Tempo Médio: {tempo_medio:.2f}s',
                  annotation_position="top left")
    fig3.show()
else:
    print("Nenhum download bem-sucedido para exibir a distribuição de tempo.")

resumo = {
    'Total Downloads': len(df),
    'Sucessos': contagem_status[contagem_status['Status'] == 'Sucesso']['Quantidade'].values[0],
    'Falhas': contagem_status[contagem_status['Status'] != 'Sucesso']['Quantidade'].values[0] if len(contagem_status) > 1 else 0,
    'Tempo Médio de Download (s)': tempo_medio if not df_sucesso.empty else 'N/A'
}

df_resumo = pd.DataFrame([resumo])

fig4 = go.Figure(data=[go.Table(
    header=dict(values=list(df_resumo.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df_resumo[col] for col in df_resumo.columns],
               fill_color='lavender',
               align='left'))
])

fig4.update_layout(title='Resumo dos Downloads')
fig4.show()

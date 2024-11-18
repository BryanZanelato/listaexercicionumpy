import numpy as np

# Definindo o tipo de dados para o dataset
datatype = [('data', 'U20'), ('regiao', 'U10'), ('produto', 'U10'),
            ('quantidade_vendida', 'i4'), ('preco_unitario', 'f4'), ('valor_total', 'f4')]

# Carregando os dados do arquivo CSV
dataset = np.genfromtxt('vendas.csv', delimiter=',', dtype=datatype, skip_header=1)

# Cálculos estatísticos do valor total de vendas
media_valor_total = np.mean(dataset['valor_total'])
mediana_valor_total = np.median(dataset['valor_total'])
desvio_valor_total = np.std(dataset['valor_total'])

# Produto com maior quantidade vendida
idx_max_quantidade = np.argmax(dataset['quantidade_vendida'])
produto_max_quantidade = dataset['produto'][idx_max_quantidade]
quantidade_max = dataset['quantidade_vendida'][idx_max_quantidade]

# Produto com maior valor total de vendas
idx_max_valor_total = np.argmax(dataset['valor_total'])
produto_max_valor_total = dataset['produto'][idx_max_valor_total]
valor_total_max = dataset['valor_total'][idx_max_valor_total]

# Calcular o valor total de vendas por região
regioes = np.unique(dataset['regiao'])
valor_total_por_regiao = np.zeros(len(regioes))

for i, regiao in enumerate(regioes):
    valor_total_por_regiao[i] = np.sum(dataset['valor_total'][dataset['regiao'] == regiao])

# Cálculo da venda média por dia
datas_unicas = np.unique(dataset['data'])
media_venda_dia = np.array([np.sum(dataset['valor_total'][dataset['data'] == data]) for data in datas_unicas])

media_venda_por_dia = np.mean(media_venda_dia)

# Determinar o dia da semana com maior número de vendas
datas = np.array([np.datetime64(data) for data in dataset['data']])
dias_da_semana = datas.astype('datetime64[D]').view('int') % 7

vendas_por_dia = np.zeros(7)
for i, dia in enumerate(dias_da_semana):
    vendas_por_dia[dia] += dataset['valor_total'][i]

dia_com_maior_venda = np.argmax(vendas_por_dia)
nome_dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

# Calcular a variação diária no valor total de vendas
dataset_ordenado = np.sort(dataset, order='data')
datas_ordenadas = np.unique(dataset_ordenado['data'])

valor_total_por_dia = np.array([np.sum(dataset_ordenado['valor_total'][dataset_ordenado['data'] == data]) 
                                for data in datas_ordenadas])

variacao_diaria = np.diff(valor_total_por_dia)

# Exibindo resultados
print("Média do valor total das vendas:", media_valor_total)
print("Mediana do valor total das vendas:", mediana_valor_total)
print("Desvio padrão do valor total das vendas:", desvio_valor_total)
print(f"Produto com maior quantidade vendida: {produto_max_quantidade} ({quantidade_max} unidades)")
print(f"Produto com maior valor total de vendas: {produto_max_valor_total} (R${valor_total_max:.2f})")
print("Valor total de vendas por região:")
for regiao, valor in zip(regioes, valor_total_por_regiao):
    print(f"  {regiao}: R${valor:.2f}")
print(f"Média de vendas por dia: R${media_venda_por_dia:.2f}")
print(f"Dia da semana com maior número de vendas: {nome_dias_da_semana[dia_com_maior_venda]}")
print("Variação diária no valor total de vendas:", variacao_diaria)

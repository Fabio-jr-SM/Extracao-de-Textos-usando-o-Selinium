# Nome do arquivo txt
file_name = 'tccs.txt'

# Lista de títulos
lista_titulos = [
    'PARQUE MÃE BONIFÁCIA',
]

# Ler o conteúdo do arquivo txt
with open(file_name, 'r', encoding='utf-8') as file:
    txt_lines = file.read().strip().split('\n')

# Contar as ocorrências de cada título na lista de linhas do arquivo txt
from collections import Counter

counter = Counter(txt_lines)

# Verificar se algum título da lista está duplicado no arquivo txt
for titulo in lista_titulos:
    if counter[titulo] > 1:
        print(f'O título "{titulo}" está duplicado no arquivo txt.')

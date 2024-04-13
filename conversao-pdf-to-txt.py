from PyPDF2 import PdfReader
import os

# Diretório onde os arquivos TCCs em PDF estão armazenados
tcc_directory = 'tccs/'

# Caminho para o arquivo de saída final em texto
output_txt_path = 'todos_tccs.txt'

# Cria uma lista para armazenar o texto de cada TCC
tcc_texts = []

# Percorre os arquivos PDF na pasta tcc_directory
for filename in os.listdir(tcc_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(tcc_directory, filename)
        
        # Cria um leitor de PDF
        pdf_reader = PdfReader(pdf_path)
        
        # Inicializa uma lista para armazenar o texto de todas as páginas de um arquivo PDF
        pdf_text = []
        
        # Extrai texto de cada página do arquivo PDF
        for page in pdf_reader.pages:
            text = page.extract_text()
            pdf_text.append(text)
        
        # Junta o texto das páginas separadas por \n\n
        full_text = '\n\n'.join(pdf_text)
        
        # Adiciona o texto do arquivo PDF à lista
        tcc_texts.append(full_text)

# Junta todo o texto dos TCCs em um único arquivo de texto
all_tccs_text = '\n\n'.join(tcc_texts)

# Salva o texto combinado em um arquivo de texto
with open(output_txt_path, 'w', encoding='utf-8') as output_file:
    output_file.write(all_tccs_text)

print(f'O arquivo de texto combinado foi salvo em: {output_txt_path}')

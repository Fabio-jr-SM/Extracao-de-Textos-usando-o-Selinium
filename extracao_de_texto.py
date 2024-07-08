from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyPDF2 import PdfReader
import time
import os
import re

def extrair_texto(tcc_directory, output_txt_path):
    """
    Extração de texto da pasta de TCCs.
    
    Args:
        tcc_directory (str): Diretório onde os TCCs em PDF estão armazenados.
        output_txt_path (str): Caminho do arquivo de saída para salvar o texto extraído.
    """
    tcc_texts = []

    # Loop através dos arquivos na pasta de TCCs
    for filename in os.listdir(tcc_directory):
        if filename.endswith('.pdf'):  # Verifica se o arquivo é um PDF
            pdf_path = os.path.join(tcc_directory, filename)
            pdf_reader = PdfReader(pdf_path)
            pdf_text = []

            # Loop através das páginas do PDF
            for page in pdf_reader.pages:
                text = page.extract_text()  # Extrai o texto da página
                pdf_text.append(text)

            full_text = '\n\n'.join(pdf_text)  # Junta o texto de todas as páginas
            tcc_texts.append(full_text)

    all_tccs_text = '\n\n'.join(tcc_texts)  # Junta o texto de todos os TCCs
    # Remove caracteres indesejados do texto extraído
    cleaned_text = re.sub(r'[^a-zA-ZáéíóúàèìòùãõâêîôûçÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÇ\s]', '', all_tccs_text)

    # Salva o texto limpo no arquivo de saída
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

    print(f'O arquivo de texto combinado foi salvo em: {output_txt_path}')

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    tcc_directory = 'tccs_revisao/'
    output_txt_path = f'tccs_extraidos_para_revisao/{nome_arquivo}.txt'

    # Extrai o texto dos TCCs baixados
    extrair_texto(tcc_directory, output_txt_path)

if __name__ == "__main__":
    main()

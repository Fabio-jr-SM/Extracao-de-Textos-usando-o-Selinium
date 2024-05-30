from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyPDF2 import PdfReader
import time
import os

# Diretório de destino para baixar os TCCs
destination_folder = r"C:\Users\fabbh\Documents\GitHub\selinium-site-turismo-tcc\tccs"

# Configurações do navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Configurar preferências de download do Chrome para definir o diretório de download
prefs = {
    "download.default_directory": destination_folder,  # Define o diretório de download
    "download.prompt_for_download": False,  # Desabilita o prompt para escolher o local de download
    "download.directory_upgrade": True,  # Permite a atualização do diretório de download
    "safebrowsing.enabled": True  # Habilita a navegação segura
}

options.add_experimental_option("prefs", prefs)

# Inicie o navegador Chrome com as opções configuradas
driver = webdriver.Chrome(options=options)

# Acesse o site
driver.get("https://turismoifmtblog.wordpress.com/tcc/")

# Aguarde a página carregar
time.sleep(3)

# Usando compreensão de lista para gerar XPaths para os links dos TCCs
tcc_xpaths = [f'//*[@id="post-173"]/div/table/tbody/tr[{i}]/td[2]/h6/a' for i in range(3, 6)]

# Percorra os três links para baixar os TCCs
for tcc_xpath in tcc_xpaths:
    # Encontre o link para o TCC usando XPath
    tcc_link = driver.find_element(By.XPATH, tcc_xpath)
    
    # Obtém a URL para o TCC
    tcc_url = tcc_link.get_attribute("href")
    
    # Abre o link
    driver.get(tcc_url)
    
    # Aguarde até que o botão de download esteja disponível na página
    wait = WebDriverWait(driver, 10)
    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div[3]/div[2]/div[2]/div[3]')))
    
    # Clica no botão de download
    download_button.click()
    
    # Aguarde o download ser iniciado (o tempo pode variar dependendo do tamanho do arquivo e da velocidade da conexão)
    time.sleep(10)
    
    # Volte para a página inicial
    driver.get("https://turismoifmtblog.wordpress.com/tcc/")
    
    # Aguarde a página carregar
    time.sleep(3)

# Fecha o navegador
driver.quit()

# Diretório onde os arquivos TCCs em PDF estão armazenados
tcc_directory = 'tccs/'

# Caminho para o arquivo de saída final em texto
output_txt_path = 'tccs_extraidos/todos_tccs.txt'

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


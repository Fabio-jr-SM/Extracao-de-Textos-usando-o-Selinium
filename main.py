from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyPDF2 import PdfReader
import time
import os
import re

def download_tccs(tcc_xpaths, destination_folder):
    """
    Baixar TCCs do Site usando o Selenium.
    
    Args:
        tcc_xpaths (list): Lista de XPaths para os TCCs a serem baixados.
        destination_folder (str): Pasta de destino para salvar os arquivos baixados.
    """
    # Configurações do navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Configurações de preferências de download
    prefs = {
        "download.default_directory": destination_folder,  # Pasta de download padrão
        "download.prompt_for_download": False,  # Não perguntar para baixar
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True  # Habilitar navegação segura
    }
    options.add_experimental_option("prefs", prefs)

    # Inicializa o WebDriver do Chrome
    driver = webdriver.Chrome(options=options)
    driver.get("https://turismoifmtblog.wordpress.com/tcc/")  # Abre a página inicial dos TCCs
    time.sleep(3)  # Espera para garantir que a página carregue completamente

    # Loop através dos XPaths dos TCCs
    for tcc_xpath in tcc_xpaths:
        tcc_link = driver.find_element(By.XPATH, tcc_xpath)  # Encontra o link do TCC
        tcc_url = tcc_link.get_attribute("href")  # Obtém o URL do link
        driver.get(tcc_url)  # Navega até a página do TCC

        wait = WebDriverWait(driver, 10)
        # Espera até que o botão de download esteja clicável e clica nele
        download_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div[3]/div[2]/div[2]/div[3]'))
        )
        download_button.click()
        
        time.sleep(10)  # Espera para garantir que o download comece
        driver.get("https://turismoifmtblog.wordpress.com/tcc/")  # Volta para a página inicial dos TCCs
        time.sleep(3)  # Espera para garantir que a página carregue completamente

    driver.quit()  # Fecha o navegador

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
    destination_folder = r"C:\Users\fabbh\Documents\GitHub\selinium-site-turismo-tcc\tccs"
    tcc_directory = 'tccs/'
    output_txt_path = 'tccs_extraidos/todos_tccs.txt'

    # XPaths específicos para TCCs 11 ao 13
    specific_tcc_xpaths = [
        '//*[@id="post-173"]/div/table/tbody/tr[13]/td[2]/h6/a[1]',
        '//*[@id="post-173"]/div/table/tbody/tr[14]/td[2]/h6/a',
        '//*[@id="post-173"]/div/table/tbody/tr[15]/td[2]/h6/span/span/span/a[1]'
    ]
    download_tccs(specific_tcc_xpaths, destination_folder)

    # XPaths para TCCs do 01 ao 10 e do 14 ao 36
    tcc_xpaths_1_10_14_36 = [f'//*[@id="post-173"]/div/table/tbody/tr[{i}]/td[2]/h6/a' for i in list(range(1, 11)) + list(range(14, 37))]
    download_tccs(tcc_xpaths_1_10_14_36, destination_folder)

    # XPaths para TCCs do 37 ao 104
    tcc_xpaths_37_104 = [f'//*[@id="post-173"]/div/div[1]/div/div/div/figure/table/tbody/tr[{i}]/td[2]/a' for i in range(1, 69)]
    download_tccs(tcc_xpaths_37_104, destination_folder)

    # Extrai o texto dos TCCs baixados
    extrair_texto(tcc_directory, output_txt_path)

if __name__ == "__main__":
    main()

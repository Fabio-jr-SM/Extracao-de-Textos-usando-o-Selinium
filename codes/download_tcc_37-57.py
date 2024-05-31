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
    Baixar TCCs do Site usando o Selenium
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    prefs = {
        "download.default_directory": destination_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://turismoifmtblog.wordpress.com/tcc/")
    time.sleep(3)

    for tcc_xpath in tcc_xpaths:
        tcc_link = driver.find_element(By.XPATH, tcc_xpath)
        tcc_url = tcc_link.get_attribute("href")
        driver.get(tcc_url)

        wait = WebDriverWait(driver, 10)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div[3]/div[2]/div[2]/div[3]')))
        download_button.click()
        
        time.sleep(10)
        driver.get("https://turismoifmtblog.wordpress.com/tcc/")
        time.sleep(3)

    driver.quit()

def extrairTexto(tcc_directory, output_txt_path):
    """
    Extração de texto da pasta de TCCs
    """
    tcc_texts = []

    for filename in os.listdir(tcc_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(tcc_directory, filename)
            pdf_reader = PdfReader(pdf_path)
            pdf_text = []

            for page in pdf_reader.pages:
                text = page.extract_text()
                pdf_text.append(text)

            full_text = '\n\n'.join(pdf_text)
            tcc_texts.append(full_text)

    all_tccs_text = '\n\n'.join(tcc_texts)

    cleaned_text = re.sub(r'[^a-zA-ZáéíóúàèìòùãõâêîôûçÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÇ\s]', '', all_tccs_text)

    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_text)

    print(f'O arquivo de texto combinado foi salvo em: {output_txt_path}')

def main():
    
    destination_folder = r"C:\Users\fabbh\Documents\GitHub\selinium-site-turismo-tcc\tccs"
    tcc_xpaths = [f'//*[@id="post-173"]/div/div[1]/div/div/div/figure/table/tbody/tr[{i}]/td[2]/a' for i in range(1,22)]

    download_tccs(tcc_xpaths, destination_folder)

    tcc_directory = 'tccs/'
    output_txt_path = 'tccs_extraidos/todos_tccs.txt'
    extrairTexto(tcc_directory, output_txt_path)

if __name__ == "__main__":
    main()

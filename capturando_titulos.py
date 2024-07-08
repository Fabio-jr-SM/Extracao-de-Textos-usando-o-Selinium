from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Configurar o webdriver do Chrome
driver = webdriver.Chrome()

# Abrir o site
url = "https://turismoifmtblog.wordpress.com/tcc/"
driver.get(url)

# Esperar a página carregar completamente
time.sleep(5)

# Função para verificar a existência de um elemento
def element_exists(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False

# Gerar XPaths dinamicamente para todos os TRs a partir de tr[1] a tr[68]
xpaths = [f'//*[@id="post-173"]/div/div[1]/div/div/div/figure/table/tbody/tr[{i}]/td[2]/a' for i in range(1, 69)]

# Extrair os títulos dos TCCs usando list comprehension
titles = [driver.find_element(By.XPATH, xpath).text for xpath in xpaths if element_exists(xpath)]

# Fechar o navegador
driver.quit()

# Salvar os títulos em um arquivo de texto
with open('tcc_titles.txt', 'w', encoding='utf-8') as file:
    for title in titles:
        file.write(title + '\n')

print("Títulos dos TCCs foram salvos em 'tcc_titles.txt'")

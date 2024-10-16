from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys

if __name__ == '__main__':
    # Configura as opções do Chrome
    chrome_options = Options()
    
    # Caso queira rodar o Chrome em modo "headless" (sem abrir a interface gráfica), descomente a linha abaixo:
    # chrome_options.add_argument("--headless")

    # Inicializa o Chrome com o ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Acessa o Looker Studio
    driver.get('https://lookerstudio.google.com/navigation/reporting?requirelogin=1')

    # LOGIN GOOGLE

    # EMAIL 
    try:
        email = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
        )
        email.send_keys("dadosguimaraes@gmail.com")
    except Exception as e:
        print(f"Erro ao inserir e-mail: {e}")
        driver.quit()
        sys.exit() 

    try:
        proxima_email = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))
        )
        proxima_email.click()
    except Exception as e:
        print(f"Erro ao clicar no botão 'Próxima' para e-mail: {e}")
        driver.quit()
        sys.exit()

    # SENHA
    try:
        senha = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
        senha.send_keys("123456oK")
    except Exception as e:
        print(f"Erro ao inserir senha: {e}")
        driver.quit()
        sys.exit() 
    sleep(2)
    try:
        proxima_senha = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))
        )
        proxima_senha.click()
    except Exception as e:
        print(f"Erro ao clicar no botão 'Próxima' para senha: {e}")
        driver.quit()
        sys.exit()
    sleep(1)
    # ABRIR O ARQUIVO PARA FAZER A CARGA
    try:
        selecionar_arquivo = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/app-bootstrap/ng2-bootstrap/lego-router-outlet/navigation-page/div/div/nav-table/ol/li[1]/div/span/nav-item/div[2]/a'))
        )
        selecionar_arquivo.click()
    except Exception as e:
        print(f"Erro ao selecionar o arquivo para carga: {e}")
        driver.quit()
        sys.exit()
    sleep(1)
    try:
        selecionar_btn_editar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="reporting-app-header"]/md-toolbar/div/product-tools-header/div/reporting-product-tools-header/edit-mode-toggle-button/button/span[2]'))
        )
        selecionar_btn_editar.click()
    except Exception as e:
        print(f"Erro ao clicar no botão 'Editar': {e}")
        driver.quit()
        sys.exit()

    sleep(2)

    try:
        selecionar_btn_carga_dados = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[2]/div/ng2-reporting-plate/plate/div/div[1]/div[1]/report-editing-tools/div/div/div/div/div[5]/icon-action-button/button/span[4]'))
        )
        selecionar_btn_carga_dados.click()
    except Exception as e:
        print(f"Erro ao clicar no botão de carga de dados: {e}")
        driver.quit()
        sys.exit()
    sleep(2)
    try:
        selecionar_btn_csv = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="google-connectors"]/div/div[2]/connector-gallery-card[7]/mat-card/div[2]/p[1]/span'))
        )
        selecionar_btn_csv.click()
    except Exception as e:
        print(f"Erro ao clicar no botão de carga de dados csv: {e}")
        driver.quit()
        sys.exit()

    # Fechar o navegador ao final
    driver.quit()
    print("Carga efetuada com sucesso!")
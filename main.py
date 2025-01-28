from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Configuração do Selenium com modo headless
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")


driver = webdriver.Chrome(options=options)

try:
    # Abre o Google
    driver.get("https://www.google.com")

    # Localiza a barra de pesquisa
    search_box = driver.find_element(By.NAME, "q")

    # Insere o termo de pesquisa e envia
    search_box.send_keys("Canvas")
    search_box.send_keys(Keys.RETURN)

    # Aguarda os resultados carregarem
    driver.implicitly_wait(10)

    # Captura os contêineres dos resultados da pesquisa
    results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")

    print("Resultados da pesquisa no Google:")
    for i, result in enumerate(results[:10], start=1):  # Limite de 10 resultados
        # Título
        title = result.find_element(By.CSS_SELECTOR, "h3").text
        # Link
        link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        print(f"{i}. {title}\n   Link: {link}")
        with open("resultados.txt", "a") as file:
            file.write(f"{i}. {title}\n   Link: {link}\n\n")

finally:
    # Fecha o navegador
    driver.quit()

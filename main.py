from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
from clean_data import to_clean_data



# abrir página
driver = WebDriver()
url = "https://www.fundamentus.com.br/fii_resultado.php"
driver.get(url)
driver.minimize_window()

# carregar dados
"""Coluna"""

table = driver.find_element(By.TAG_NAME, "table")
thead = table.find_element(By.TAG_NAME, "thead")
header = thead.find_element(By.TAG_NAME, "tr")
th = header.find_elements(By.TAG_NAME, "th")

"""linha"""

tbody = driver.find_element(By.XPATH, "//*[@id='tabelaResultado']/tbody")



# extrair dados
columns = []
rows = []

for i in th:
    if i.text.strip():
        columns.append(i.text)


for tr in tbody.find_elements(By.TAG_NAME, "tr"):
    data = []
    for i in tr.find_elements(By.TAG_NAME, "td"):
        if i.text.strip():
            data.append(i.text)

        elif not i.text.strip() and len(data)<13:
            data.append(None)

    rows.append(data)

# limpar dados
df_hard = pd.DataFrame(data=rows, columns=columns)
data_clean = to_clean_data(df_hard)



# salvar num arquivo csv
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")

data_clean.to_csv(f"./data/report_{timestamp}.csv", index=False, sep=";")
from playwright.sync_api import sync_playwright
from time import sleep
import os
import pandas as pd


download_path = os.path.join(os.getcwd(), "Files")
os.makedirs(download_path, exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://infoms.saude.gov.br/extensions/covid-19_html/covid-19_html.html#")
    sleep(5)


    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.locator("#exportar-dados-QV1-Casos-01").click()
        page1 = page1_info.value
    download = download_info.value
    casos_path = os.path.join(download_path, "Casos.xlsx")
    download.save_as(casos_path)
    page1.close()


    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.locator("#exportar-dados-QV1-Obitos-01").click()
        page2 = page2_info.value
    download1 = download1_info.value
    obitos_path = os.path.join(download_path, "Obitos.xlsx")
    download1.save_as(obitos_path)
    page2.close()

    sleep(2)
    browser.close()


print("\n📊 Visualizando os dados de Casos:")
df_casos = pd.read_excel(casos_path)
print(df_casos)

print("\n📊 Visualizando os dados de Óbitos:")
df_obitos = pd.read_excel(obitos_path)
print(df_obitos)

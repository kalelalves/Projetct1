from playwright.sync_api import sync_playwright
from time import sleep
import os

# Caminho onde os arquivos serão salvos
download_path = r"C:\Users\Kalel\PycharmProjects\PythonProject1\Files"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://infoms.saude.gov.br/extensions/covid-19_html/covid-19_html.html#")
    sleep(5)

    # Primeiro download - Casos
    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.locator("#exportar-dados-QV1-Casos-01").click()
        page1 = page1_info.value
    download = download_info.value
    download.save_as(os.path.join(download_path, "Casos.xlsx"))
    page1.close()

    # Segundo download - Óbitos
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.locator("#exportar-dados-QV1-Obitos-01").click()
        page2 = page2_info.value
    download1 = download1_info.value
    download1.save_as(os.path.join(download_path, "Obitos.xlsx"))
    page2.close()

    sleep(5)
    browser.close()

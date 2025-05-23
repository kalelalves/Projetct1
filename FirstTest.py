import re
from calendar import isleap
from time import sleep

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://infoms.saude.gov.br/extensions/covid-19_html/covid-19_html.html#")
    sleep(5)
    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.locator("#exportar-dados-QV1-Casos-01").click()
        page1 = page1_info.value
    download = download_info.value
    page1.close()
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.locator("#exportar-dados-QV1-Obitos-01").click()
        page2 = page2_info.value
    download1 = download1_info.value
    page2.close()
    sleep(50)

    # ---------------------
    context.close()
    browser.close()



with sync_playwright() as playwright:
    run(playwright)
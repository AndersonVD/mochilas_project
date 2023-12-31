from bs4 import BeautifulSoup
import json
import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_sync
import requests

BASE_URL = "https://www.nike.com.br"
url = "https://www.nike.com.br/nav/categorias/bolsasmochilas/genero/masculino/idade/adulto/tipodebolsasmochilas/mochilas/tipodeproduto/acessorios"
IMAGE_URL = "https://imgnike-a.akamaihd.net/1200x1200/{}.jpg"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36",
    "accept-language": "en-US,en;q=0.5",  # Defina o idioma de preferência
}


# run playwright install chromium
async def nike_spider():
    try:
        # p = await async_playwright().start()
        # browser = await p.chromium.launch()
        # context = await browser.new_context(
        #     user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4454.0 Safari/537.36"
        # )
        # page = await context.new_page()
        # stealth_sync(page)
        # await page.goto(url)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        # await browser.close()

        backpack = []

        data = soup.find("script", {"id": "__NEXT_DATA__"}).contents[0]
        data = json.loads(data)
        products = data["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"][
            "data"
        ]["pages"][0]["products"]

        for product in products:
            backpack.append(
                {
                    "name": product["name"],
                    "price": product["price"],
                    "link": BASE_URL + product["url"],
                    "image": IMAGE_URL.format(product["id"]),
                }
            )

        return backpack
    except Exception as e:
        print(e)
        return {"error": e}


if __name__ == "__main__":
    asyncio.run(nike_spider())

import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.nike.com.br"
url = "https://www.nike.com.br/nav/categorias/bolsasmochilas/genero/masculino/idade/adulto/tipodebolsasmochilas/mochilas/tipodeproduto/acessorios"
IMAGE_URL = "https://imgnike-a.akamaihd.net/1200x1200/{}.jpg"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
}


async def adidas_spider():
    response = requests.request("GET", url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
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

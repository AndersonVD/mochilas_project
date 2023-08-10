import httpx
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.nike.com.br"
url = "https://www.nike.com.br/nav/categorias/bolsasmochilas/genero/masculino/idade/adulto/tipodebolsasmochilas/mochilas/tipodeproduto/acessorios"
IMAGE_URL = "https://imgnike-a.akamaihd.net/1200x1200/{}.jpg"

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "accept-language": "en-US,en;q=0.5",  # Defina o idioma de preferência
}


async def nike_spider():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # Verificar se a resposta é bem-sucedida
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

        except httpx.RequestError as e:
            print(f"Erro na requisição: {e}")
            return ["Erro na requisição"]


if __name__ == "__main__":
    import asyncio

    async def main():
        backpack = await nike_spider()
        print(backpack)

    asyncio.run(main())

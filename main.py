from fastapi import FastAPI
from adidas_spider import adidas_spider

app = FastAPI(
    title="Verificador De Mochilinhas ",
    description="Buscador de dados feito pode adersonvd.com",
    version="1.0.0",
    docs_url="/",
)


@app.get("/api/v1/backpack")
async def get_backpack_data():
    return await adidas_spider()

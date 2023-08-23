from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.nike_spider import nike_spider

app = FastAPI(
    title="Verificador De Mochilinhas ",
    description="Buscador de dados feito pode adersonvd.com",
    version="1.0.0",
    docs_url="/",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/backpack")
async def get_backpack_data():
    dados = await nike_spider()
    return dados

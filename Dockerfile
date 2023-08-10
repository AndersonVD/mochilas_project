# syntax = docker/dockerfile:1.4

# Etapa 1: Construir a imagem base do aplicativo FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /app

# Copiar o arquivo de requisitos e instalar dependências
COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Copiar o diretório do aplicativo
COPY ./app ./app

# Etapa 2: Definir variáveis de ambiente e instalar ferramentas adicionais
FROM builder as dev-envs

RUN apt-get update \
    && apt-get install -y --no-install-recommends git

RUN useradd -s /bin/bash -m vscode \
    && groupadd docker \
    && usermod -aG docker vscode

# Etapa 3: Copiar ferramentas do Docker (CLI, buildx, compose)
COPY --from=gloursdocker/docker / /

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

# Etapa 2: Definir variáveis de ambiente
ENV LOGLEVEL="info"
ENV WORKERS=8
ENV BIND="0.0.0.0:10000"
ENV GRACEFUL_TIMEOUT=120
ENV TIMEOUT=120
ENV KEEPALIVE=5
ENV ERRORLOG="-"
ENV ACCESSLOG="-"
ENV WORKERS_PER_CORE=1.0
ENV USE_MAX_WORKERS="null"
ENV HOST="0.0.0.0"
ENV PORT="10000"

# Etapa 3: Executar o servidor Gunicorn
CMD ["gunicorn", "app.main:app", "--log-level", "$LOGLEVEL", "-w", "$WORKERS", "-b", "$BIND", "--graceful-timeout", "$GRACEFUL_TIMEOUT", "--timeout", "$TIMEOUT", "--keep-alive", "$KEEPALIVE", "--error-logfile", "$ERRORLOG", "--access-logfile", "$ACCESSLOG", "--workers-per-core", "$WORKERS_PER_CORE", "--use-max-workers", "$USE_MAX_WORKERS"]

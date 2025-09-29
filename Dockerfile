# Use a imagem oficial do Python
FROM python:3.13-slim

# Instalar dependências do sistema, incluindo readline
RUN apt-get update && apt-get install -y \
    locales \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    shared-mime-info \
    libgirepository-1.0-1 \
    libreadline-dev \
    libncurses5-dev \
    && rm -rf /var/lib/apt/lists/*

# Configurar e gerar o locale corretamente
RUN echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Definir as variáveis de ambiente do locale
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL=pt_BR.UTF-8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de dependências (requirements.txt) para o container
COPY requirements.txt /app/

# Instale as dependências do Python
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto do código do projeto para o container
COPY . /app/

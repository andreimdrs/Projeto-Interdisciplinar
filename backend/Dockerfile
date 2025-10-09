# Usar uma imagem oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY ./app /app

# Expor a porta que o FastAPI irá rodar (neste caso, 8000)
EXPOSE 8000

# Comando para iniciar a aplicação com Uvicorn
# O --host 0.0.0.0 permite que a aplicação seja acessível de fora do contêiner
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
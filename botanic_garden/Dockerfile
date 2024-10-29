# Dockerfile para Django

FROM python:3.10

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependência e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar Gunicorn
RUN pip install gunicorn

# Copiar o restante do código da aplicação
COPY . .
RUN python manage.py collectstatic --noinput
# Expor a porta que o Django vai rodar
EXPOSE 8000

# Comando para iniciar o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "botanic_garden.wsgi:application"]

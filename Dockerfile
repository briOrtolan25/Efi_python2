# imagen de la distro de Linux
FROM python:alpine3.19
#imagen de Python y distro linux que vamos a usar

# Copia todo lo del directorio en el contenedor
COPY . /app

# Setea el directorio de trabajo en el contenedor
WORKDIR /app

# Corre comandos
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone puerto
EXPOSE 5006

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


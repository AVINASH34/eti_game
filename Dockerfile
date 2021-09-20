FROM python:3.7

COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Installs pip requirements and copy entire app over!
RUN pip install -r requirements.txt
RUN pip install termcolor
COPY . /app

ENV DISPLAY=:99

COPY . /app
WORKDIR /app
CMD ["python", "game.py"]
CMD ["python", "game.py"]
CMD ["python", "game.py"]
FROM python:3.9-slim
FROM python:3.9-slim
CMD ["python", "game.py"]
FROM python:3.9-slim
COPY . /app
FROM python:3.9-slim
RUN pip install requirements.txt
WORKDIR /app
RUN pip install requirements.txt
COPY . /app
CMD ["python", "game.py"]
FROM python:3.9-slim
FROM python:3.9-slim
CMD ["python", "game.py"]
WORKDIR /app
CMD ["python", "game.py"]

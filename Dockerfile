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

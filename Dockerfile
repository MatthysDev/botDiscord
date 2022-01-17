FROM python:3

RUN mkdir -p /APP/Github/botDocker
WORKDIR /APP/Github/botDocker
RUN pip install discord

COPY . .



CMD ["python", "discordbot.py"]
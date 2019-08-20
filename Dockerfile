FROM ubuntu:latest

WORKDIR /app
COPY . /app

EXPOSE 5000

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP="app.py"

RUN apt-get update && apt-get install -y \
    python3-flask \
    python3-pytango

CMD ["flask", "run",  "--host=0.0.0.0"]
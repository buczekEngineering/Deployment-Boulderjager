FROM python:3.9.7-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && apt-get clean

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
COPY static /static

RUN pip install -r /app/requirements.txt

COPY . /app/

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

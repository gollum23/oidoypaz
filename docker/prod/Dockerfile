FROM python:3.8

COPY base.txt /tmp/base.txt
COPY prod.txt /tmp/prod.txt
RUN pip install -r /tmp/prod.txt

COPY run-production.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/run-production.sh

WORKDIR /app

CMD ["run-production.sh"]

FROM python:2.7-alpine3.6
ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache \
    build-base \
    mariadb-dev \
    py-mysqldb \
    linux-headers
RUN pip install --no-cache-dir uwsgi
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD mysql_timeout /code/
ADD docker/uwsgi.ini /etc/uwsgi.ini
CMD ["uwsgi", "/etc/uwsgi.ini"]
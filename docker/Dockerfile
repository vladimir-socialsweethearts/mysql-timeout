FROM python:alpine3.6
ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache \
    libffi-dev \
    build-base \
    postgresql-dev \
    linux-headers \
    zlib-dev \
    jpeg-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
ADD mysql_timeout /code/
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
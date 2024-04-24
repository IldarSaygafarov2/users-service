FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /test-app
WORKDIR /test-app
COPY . /test-app/
RUN pip install -r requirements.txt

FROM python:3.7-alpine
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
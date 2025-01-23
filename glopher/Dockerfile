FROM python:3.10.16-alpine as base

WORKDIR /glopher
RUN apk upgrade

COPY requirements/requirements.txt requirements/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements/requirements.txt

COPY . .
RUN python -m pip install -e .

ENV PYTHONPATH=/glopher
ENV HOME=/glopher

FROM base as dev

RUN apk add bash
RUN apk add neovim

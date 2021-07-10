# syntax=docker/dockerfile:1
# FROM ubuntu:20.04
FROM python:3.8-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN apt-get update
#     apt-get install --no-install-recommends -y \
#     python3.8 python3-pip python3.8-dev
RUN apt-get install tesseract-ocr -y
RUN pip3 install PyMuPDF-1.18.14-cp38-cp38-manylinux2010_x86_64.whl
RUN pip3 install -r requirements.txt

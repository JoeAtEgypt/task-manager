FROM python:3.11.0-alpine

ENV SECRET_KEY='*p508deyenp28ajnmork-1xk%9x-l3h8sc3#$#n7nwkrdz24@0'

WORKDIR /app

COPY req.txt /app/

RUN apk update &&  apk add postgresql-dev gcc python3-dev musl-dev \
    py3-setuptools tiff-dev jpeg-dev openjpeg-dev zlib-dev \
    freetype-dev lcms2-dev libwebp-dev tcl-dev tk-dev harfbuzz-dev \
    fribidi-dev libimagequant-dev libxcb-dev libpng-dev \
    py3-magic                                           # versatile image dependencies

RUN pip install --upgrade pip

RUN pip install -r req.txt

COPY . /app

EXPOSE 1000

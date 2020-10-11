FROM moss/xelatex as xelatex
FROM vikingco/jinja2cli:latest as jinja2cli
FROM ubuntu:latest as ubuntu
RUN apt update && apt install -y qrencode imagemagick

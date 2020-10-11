#!/usr/bin/env bash
mkdir -p ./project/out
docker-compose run python make_message.py
docker-compose run qr -lH -o qrcode.png -r message.txt
docker-compose run convert qrcode.png qrcode.jpg
docker-compose run xelatex -output-directory=/project/out bisturbile_defence_matrix.tex

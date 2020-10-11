#!/usr/bin/env bash
mkdir -p ./project/out
docker run -v `pwd`:/project -w /project/tex moss/xelatex xelatex -output-directory=/project/out bare_adv.tex

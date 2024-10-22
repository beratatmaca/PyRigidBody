#!/usr/bin/env bash
lazydocs \
    --output-path="./docs/docstrings" \
    --overview-file="README.md" \
    --src-base-url="https://github.com/<you github account>/<your repo>/blob/master/" \
    ./src

mkdocs build
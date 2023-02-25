# Cookbook

Simple web app to collect and share cooking recipes. 

## Setup
```sh
poetry install
```

## Run
```sh
poetry shell
docker-compose up -d
uvicorn app.main:app --reload
```

## Interactive shell
```sh
export PYTHONPATH=$PYTHONPATH:`pwd`
python -i app/main.py
```
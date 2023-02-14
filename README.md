# Cookbook

Simple web app to collect and share cooking recipes. 

## Setup
```sh
python -m venv local
source local/bin/activate
pip install -r requirements.txt
```

## Run
```sh
docker-compose up -d
uvicorn app.main:app --reload
```

## Interactive shell
```sh
export PYTHONPATH=$PYTHONPATH:`pwd`
python -i app/main.py
```
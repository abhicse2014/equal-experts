# GitHub Gists API

## Run
pip install -r requirements.txt
uvicorn app.main:app --port 8080

## Test
python -m pytest -v

## Docker
docker build -t github-gists-api .
docker run -p 8080:8080 github-gists-api

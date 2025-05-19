PORT ?= 8000
install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run --port 8000 

start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

lint:
	uv run ruff check 

render-start:
	uv run python3 -m page_analyzer.db.database
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build-db:
	uv run python3 -m page_analyzer.db.database

build: install build-db

prod:
	docker run -it -e 'DATABASE_URL=${DATABASE_URL}' -p 8000:8000 page_analyzer:latest

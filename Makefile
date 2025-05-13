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
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build:
	./build.sh

prod:
	docker compose down
	docker compose build
	docker compose up

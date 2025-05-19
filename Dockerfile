FROM python:3.12-slim

RUN apt-get update && apt-get install -yqq \
    make \
    sudo \
    curl
    
RUN pip install uv

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

COPY . .

CMD ["make", "render-start"]
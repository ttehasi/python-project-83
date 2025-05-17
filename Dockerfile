FROM python:3.12-slim

RUN apt-get update && apt-get install -yqq \
    make \
    # postgresql-15 \
    sudo \
    curl
    
RUN pip install uv

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

COPY . .

# postgres config
# RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/15/main/pg_hba.conf && \
#     echo "listen_addresses='*'" >> /etc/postgresql/15/main/postgresql.conf

# create docker user and db
# RUN service postgresql start && \
#     su postgres -c "psql --command \"CREATE USER docker WITH SUPERUSER PASSWORD 'docker';\"" && \
#     su postgres -c "createdb -O docker docker" && \
#     service postgresql stop


CMD ["make", "render-start"]
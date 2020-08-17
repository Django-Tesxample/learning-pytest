ARG PYTHON_VERSION=3.8


#####################BASE######################
FROM python:${PYTHON_VERSION} as base

RUN mkdir /app
RUN mkdir /config
WORKDIR /app
# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY ./src/ /app

#####################PRODUDCTION######################
FROM base as prod

WORKDIR /app
COPY ./src/ /app
COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY ./docker-entrypoint.sh /root
RUN chmod +x /root/docker-entrypoint.sh

EXPOSE 8000
#ENTRYPOINT ["/root/docker-entrypoint.sh"]
#HEALTHCHECK CMD curl -f http://localhost/ || exit 1
CMD tail -f



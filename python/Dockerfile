FROM python:latest as dev

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /code
COPY pyproject.toml .
COPY poetry.toml .

RUN $HOME/.poetry/bin/poetry install --no-root


FROM base as prod
COPY {{ project }} ./{{ project }}

RUN $HOME/.poetry/bin/poetry install

ENTRYPOINT [ "entrypoint" ]
FROM python:latest as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV HOME="/root"
ENV PATH="$HOME/.poetry/bin:$PATH"

FROM base as dev

WORKDIR /code
COPY pyproject.toml .
COPY poetry.toml .

RUN poetry install --no-root


FROM dev as prod
COPY {{ project }} ./{{ project }}

RUN $HOME/.poetry/bin/poetry install

ENTRYPOINT [ "entrypoint" ]
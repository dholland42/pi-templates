FROM python:3.10 as base

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

ENV HOME="/root"
ENV PATH="$HOME/.local/bin:$PATH"

FROM base as dev

WORKDIR /code

COPY pyproject.toml .
COPY poetry.toml .

RUN poetry install --no-root

FROM dev as prod

COPY {{ project }} ./{{ project }}

RUN poetry install

ENTRYPOINT [ "entrypoint" ]
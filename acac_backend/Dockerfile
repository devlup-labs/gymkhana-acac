FROM python:3.6-alpine

ARG BUILD_DEPS="gcc python3-dev musl-dev postgresql-dev libffi-dev jpeg-dev zlib-dev libjpeg libmagic"
RUN apk --no-cache add ${BUILD_DEPS}
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install celery
COPY Pipfile* Pipfile.lock* ./
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy --ignore-pipfile --dev \
    && find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' \+

WORKDIR /app
COPY . /app
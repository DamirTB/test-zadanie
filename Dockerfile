FROM python:3.12-slim

LABEL maintainer="Damir Talipov"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc libpq-dev build-essential libjpeg-dev zlib1g-dev libssl-dev && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get remove -y gcc build-essential && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp && \
    adduser --disabled-password --no-create-home django-user && \
    mkdir -p /vol/web/media /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol 

ENV PATH="/py/bin:$PATH"

USER django-user

CMD ["run.sh"]

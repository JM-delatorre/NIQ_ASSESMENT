
FROM python:3.12.4-alpine AS build-stage


RUN apk update && \
    apk add build-base libpq libpq-dev

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"


WORKDIR /app

COPY app /app

RUN pip install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

# ----------------------------

FROM python:3.12.4-alpine AS run-stage

RUN apk update \
    && apk upgrade \
    && apk add --no-cache libpq 

WORKDIR /app

COPY --from=build-stage /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY --from=build-stage /app /app


EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
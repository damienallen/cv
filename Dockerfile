FROM python:3.12-slim-trixie AS cv-builder
RUN apt-get update && apt-get install -y weasyprint
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . .
RUN uv sync
RUN uv run python -m cv.generate

FROM joseluisq/static-web-server:2-alpine AS server
ENV SERVER_ROOT=/public
ENV SERVER_PORT=8080

COPY --from=cv-builder dist/ /public
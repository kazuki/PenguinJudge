FROM python:3.8-slim

COPY . /work
RUN cd /work && pip install . && cd / && rm -rf ~/.cache /work

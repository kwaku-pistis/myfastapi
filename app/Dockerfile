FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir -p /app/app
COPY ./app/*  /app/app/

RUN ls /app/app

ENV PYTHONPATH=/app/app


RUN echo $PYTHONPATH
RUN pip install -r /app/app/requirements.txt
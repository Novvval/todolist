FROM python:3.10-slim

WORKDIR .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off
COPY . .
CMD python ./todolist/manage.py runserver 0.0.0.0:8000


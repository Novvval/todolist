FROM python:3.10-slim

WORKDIR opt/todolist
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=opt/todolist
COPY . .
CMD python ./todolist/manage.py runserver 0.0.0.0:8000


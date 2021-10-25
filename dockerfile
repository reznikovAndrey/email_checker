FROM python:3.9.7

WORKDIR /code
COPY requirements.txt /code
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code
CMD uvicorn app.app:app --reload --host 0.0.0.0 --port 8000
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY=${SECRET_KEY}

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
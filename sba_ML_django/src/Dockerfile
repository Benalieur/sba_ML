FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY=${SECRET_KEY}

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate
    

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
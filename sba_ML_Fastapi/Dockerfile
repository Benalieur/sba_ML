FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app
COPY models/GradientBoostingClassifier.pkl app/models/GradientBoostingClassifier.pkl

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "api.py" ]
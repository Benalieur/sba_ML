FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app
COPY sba_ML_Fastapi/models/GradientBoostingClassifier.pkl /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "api.py" ]
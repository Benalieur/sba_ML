FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . .
COPY sba_ML_Fastapi/models/GradientBoostingClassifier.pkl myapp/models/GradientBoostingClassifier.pkl

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "python", "api.py" ]
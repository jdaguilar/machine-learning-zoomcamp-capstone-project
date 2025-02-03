FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/creditability_app src/creditability_app

EXPOSE 5000

ENV FLASK_APP=src/creditability_app/app.py

CMD ["flask", "run", "--host=0.0.0.0"]

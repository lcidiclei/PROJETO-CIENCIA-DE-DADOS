FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install pandas numpy matplotlib scikit-learn mlflow joblib fastapi uvicorn

CMD ["python", "src/pipeline.py"]

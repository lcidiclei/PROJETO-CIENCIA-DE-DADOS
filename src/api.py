app = FastAPI()

modelo = joblib.load("models/modelo.pkl")

@app.get("/")
def home():
    return {"status": "API funcionando"}

@app.post("/predict")
def predict(features: dict):

    df = pd.DataFrame([features])

    previsao = modelo.predict(df)

    return {
        "previsao": float(previsao[0])
    }

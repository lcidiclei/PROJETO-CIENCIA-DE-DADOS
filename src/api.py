from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "API Online"
    }


@app.post("/prever")
def prever(dados: dict):
    return {
        "mensagem": "Implementar previsão usando o modelo treinado"
    }

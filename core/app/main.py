from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Sync V1.0 rodando com UV e FastAPI!"}
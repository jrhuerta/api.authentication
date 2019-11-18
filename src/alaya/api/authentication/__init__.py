from fastapi import FastApi

app = FastAPI()

@app.post()
def login(username: str, password: str):
    return {"message": "OK"}
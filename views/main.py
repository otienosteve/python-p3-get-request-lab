from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_all() -> None:
    return {"message" : "Welcome to Kenya"}

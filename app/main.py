from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello() -> dict[str, str]:
    return {
        "MESSAGE": "Hello World with FastAPI from Traefik!"
    }
from os import listdir
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/ls")
def ls():
    return {"files": os.listdir()}

@app.get("/create")
def create():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    with open(f"{dt_string}.txt", "w") as f:
        f.write("Hello")

    return 200

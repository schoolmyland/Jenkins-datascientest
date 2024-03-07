from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "We Love Datascience, and we did it i think so. We build a CI/CD Pipeline !!"}

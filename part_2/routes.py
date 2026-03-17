from fastapi import FastAPI
from queries import Queries

app = FastAPI()


@app.get("/q1")
def mooving_alert():
    responce = Queries.query_1_mooving_alert()
    
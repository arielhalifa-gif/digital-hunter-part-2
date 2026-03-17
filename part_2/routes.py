from fastapi import FastAPI
import uvicorn
from queries import Queries

app = FastAPI()


@app.get("/q1")
def mooving_alert():
    response = Queries.query_1_mooving_alert()
    return response


@app.get("/q2")
def count_signal_type():
    response = Queries.query_2_count_signal_type()
    return response


@app.get("/q3")
def top_3_unknown():
    response = Queries.query_3_top_3_unknown()
    return response


@app.get("/q4")
def waking_up():
    response = Queries.query_4_waking_up()
    return response




if __name__ == "__routes__":
    uvicorn.run("routes:app",host="localhost", port=8000)
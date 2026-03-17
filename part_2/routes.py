from fastapi import FastAPI

app = FastAPI()


@app.get("/q1")
def mooving_alert():
    pass
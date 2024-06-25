from fastapi import FastAPI

app = FastAPI()

@app.get("/foo")
def foo_endpoint():
    return {"message": "This is a message from the foo endpoint"}

@app.get("/bar")
def bar_endpoint():
    return {"message": "This is a message from the bar endpoint"}
# File: main.py
from fastapi import FastAPI, Query, HTTPException
import random

# Import the service
from logic_service import get_random_number

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get('/')
async def read_root(number: int = Query(None), test: str = Query(None)):
    if number is None:
        number = get_random_number()
    expected_test = 'even' if number % 2 == 0 else 'odd'
    if test is not None and test != expected_test:
        raise HTTPException(status_code=400, detail=f"Invalid 'test' value. Expected '{expected_test}' but got '{test}'")
    return {'foo': 'bar', 'number': number, 'test': expected_test}

# Define a route for the server status endpoint
@app.get('/status')
async def get_status():
    return {'status': 'Server is running'}

# Define a route for the hello endpoint
@app.get('/hello')
async def say_hello():
    return {'message': 'Hello, World!'}

# Define a route for the test endpoint
@app.get('/test')
async def get_joke():
    jokes = [
        ("Why don't scientists trust atoms? Because they make up everything!", 10),
        ("Why did the scarecrow win an award? Because he was outstanding in his field!", 30),
        ("Why don't skeletons fight each other? They don't have the guts.", 60)
    ]
    joke = random.choices([j[0] for j in jokes], weights=[j[1] for j in jokes], k=1)[0]
    return {'joke': joke}

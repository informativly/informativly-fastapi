from fastapi import FastAPI, Query, HTTPException

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
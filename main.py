# Import FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Import the service
from .logic_service import get_random_number

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
async def read_root():
    random_number = get_random_number()
    return {"foo": "bar", "number": random_number}

# Define a route for the server status endpoint
@app.get("/status")
async def get_status():
    return {"status": "Server is running"}

# Define a new route for the hello world HTML page
@app.get("/hello", response_class=HTMLResponse)
async def get_hello_world():
    html_content = "<html><body><h1>Hello World</h1></body></html>"
    return HTMLResponse(content=html_content, status_code=200)

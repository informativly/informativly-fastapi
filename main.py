# Import FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
async def read_root():
    return {"Hello": "World champions"}

# Define a route for the server status endpoint
@app.get("/status")
async def get_status():
    return {"status": "Server is running"}

# Define a new route for the hello world HTML page
@app.get("/hello", response_class=HTMLResponse)
async def get_hello_world():
    html_content = "<html><body><h1>Hello World</h1></body></html>"
    return HTMLResponse(content=html_content, status_code=200)

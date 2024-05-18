# Import FastAPI
from fastapi import FastAPI

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

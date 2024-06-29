from fastapi import FastAPI, Query, HTTPException
import random
from fastapi.middleware.cors import CORSMiddleware

# Import the service
from logic_service import get_random_number

# Create an instance of the FastAPI class
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Define a route for the jokes endpoint
@app.get('/jokes')
async def get_jokes():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the math book look sad? Because it had too many problems.",
        "Why was the math lecture so long? The professor kept going off on a tangent.",
        "Why did the computer go to the doctor? Because it had a virus!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why don't some couples go to the gym? Because some relationships don't work out."
    ]
    return {'jokes': jokes}

@app.get('/random_joke')
async def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the math book look sad? Because it had too many problems.",
        "Why was the math lecture so long? The professor kept going off on a tangent.",
        "Why did the computer go to the doctor? Because it had a virus!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why don't some couples go to the gym? Because some relationships don't work out."
    ]
    joke = random.choice(jokes)
    return {'joke': joke}
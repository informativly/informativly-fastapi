from fastapi import FastAPI, Query, HTTPException
import random
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from fastapi.staticfiles import StaticFiles

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

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')
if not os.path.exists('static/js'):
    os.makedirs('static/js')

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a route for the root endpoint
@app.get('/')
async def read_root():
    return FileResponse('static/index.html')

# Define a route for the server status endpoint
@app.get('/status')
async def get_status():
    return {'status': 'Server is running'}

# Define a route for the hello endpoint
@app.get('/hello')
async def say_hello():
    return {'message': 'Hello, World!'}

# Define a route for the jokes page
@app.get('/jokes')
async def jokes_page():
    return FileResponse('static/jokes.html')

# Define a route for the riddles page
@app.get('/riddles')
async def riddles_page():
    return FileResponse('static/riddles.html')

# Define a route for the jokes endpoint
@app.get('/api/jokes')
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

@app.get('/api/random_joke')
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
    joke1 = random.choice(jokes)
    joke2 = random.choice(jokes)
    while joke1 == joke2:
        joke2 = random.choice(jokes)
    return {'jokes': [joke1, joke2]}

@app.get('/api/riddles')
async def get_riddles():
    riddles = [
        {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "answer": "An echo"},
        {"question": "You measure my life in hours and I serve you by expiring. I'm quick when I'm thin and slow when I'm fat. The wind is my enemy. What am I?", "answer": "A candle"},
        {"question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", "answer": "A map"},
        {"question": "What has keys, but no locks; space, but no room; you can enter, but not go in?", "answer": "A keyboard"},
        {"question": "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by everyone. What am I?", "answer": "A pencil lead"},
        {"question": "I have branches, but no fruit, trunk or leaves. What am I?", "answer": "A bank"},
        {"question": "What is always in front of you but can't be seen?", "answer": "The future"},
        {"question": "What can travel around the world while staying in a corner?", "answer": "A stamp"},
        {"question": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "answer": "Fire"},
        {"question": "The more you take, the more you leave behind. What am I?", "answer": "Footsteps"}
    ]
    return {'riddles': riddles}
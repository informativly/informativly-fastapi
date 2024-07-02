document.addEventListener('DOMContentLoaded', function() {
    const jokeButton = document.getElementById('get-joke');
    const jokeDisplay = document.getElementById('joke-display');

    jokeButton.addEventListener('click', async function() {
        try {
            const response = await fetch('/random_joke');
            const data = await response.json();
            jokeDisplay.innerHTML = `1. ${data.jokes[0]}<br><br>2. ${data.jokes[1]}`;
        } catch (error) {
            console.error('Error fetching jokes:', error);
            jokeDisplay.textContent = 'Oops! Failed to fetch jokes. Please try again.';
        }
    });
});
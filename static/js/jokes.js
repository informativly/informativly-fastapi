document.addEventListener('DOMContentLoaded', function() {
    const jokeButton = document.getElementById('get-joke');
    const jokeDisplay = document.getElementById('joke-display');

    jokeButton.addEventListener('click', async function() {
        const response = await fetch('/random_joke');
        const data = await response.json();
        jokeDisplay.textContent = `${data.jokes[0]}\n${data.jokes[1]}`;
    });
});
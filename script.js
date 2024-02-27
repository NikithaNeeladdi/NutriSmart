document.getElementById('generateForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const ingredientsInput = document.getElementById('ingredients').value;
    fetch('<YOUR_FLASK_APP_URL>/generate_recipe', {  // Replace <YOUR_FLASK_APP_URL> with your deployed Flask app URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients: ingredientsInput })
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('recipePrompt').innerText = data;
    })
    .catch(error => console.error('Error:', error));
});

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('generate-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const prompt = document.getElementById('prompt').value;

        fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({prompt: prompt}),
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<h2>Generated Text:</h2><p>${data.generated_text}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = `<p>An error occurred: ${error}</p>`;
        });
    });
});
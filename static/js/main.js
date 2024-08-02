document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('generate-form');
    const resultDiv = document.getElementById('result');
    const speakButton = document.getElementById('speak-button');
    const audioPlayer = document.getElementById('audio-player');

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
            speakButton.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = `<p>An error occurred: ${error}</p>`;
        });
    });

    speakButton.addEventListener('click', function() {
        const generatedText = resultDiv.querySelector('p').textContent;

        fetch('/api/text-to-speech', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({text: generatedText}),
        })
        .then(response => response.blob())
        .then(blob => {
            const audioUrl = URL.createObjectURL(blob);
            audioPlayer.src = audioUrl;
            audioPlayer.style.display = 'block';
            audioPlayer.play();
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML += `<p>An error occurred while generating speech: ${error}</p>`;
        });
    });
});
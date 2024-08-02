from flask import jsonify, request, send_file
from api import app, db
from api.models import GeneratedContent
from ai_engine.inference import generate_content
from gtts import gTTS
import os
import tempfile

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    generated_text = generate_content(prompt)
    
    new_content = GeneratedContent(prompt=prompt, generated_text=generated_text)
    db.session.add(new_content)
    db.session.commit()
    
    return jsonify({'generated_text': generated_text}), 200

@app.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio:
        tts = gTTS(text=text, lang='en')
        tts.save(temp_audio.name)
    
    return send_file(temp_audio.name, mimetype='audio/mp3')
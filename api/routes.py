from flask import jsonify, request
from api import app, db
from api.models import GeneratedContent
from ai_engine.inference import generate_content
from ai_engine.model import GenAIModel

# Initialize the model with the fine-tuned weights
gen_ai_model = GenAIModel(model_path='./fine_tuned_model')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    generated_text = gen_ai_model.generate(prompt)
    
    new_content = GeneratedContent(prompt=prompt, generated_text=generated_text)
    db.session.add(new_content)
    db.session.commit()
    
    return jsonify({'generated_text': generated_text}), 200

@app.route('/api/history', methods=['GET'])
def get_history():
    history = GeneratedContent.query.order_by(GeneratedContent.created_at.desc()).limit(10).all()
    return jsonify([{'prompt': h.prompt, 'generated_text': h.generated_text, 'created_at': h.created_at} for h in history]), 200
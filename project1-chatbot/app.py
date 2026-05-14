"""
DecodeLabs - Project 1 | Phase 1: Foundation
Flask Backend - MVP Implementation
"""

from flask import Flask, render_template, request, jsonify
from chatbot import RuleBasedChatbot
from datetime import datetime

app = Flask(__name__)

# Initialize deterministic logic engine
chatbot = RuleBasedChatbot()

@app.route('/')
def index():
    """Serve the chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API: Process user message through logic engine"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'response': 'Please type a message.', 'type': 'error'})

        # Process through deterministic engine
        response = chatbot.process_input(user_message)

        # Check for exit
        exit_cmds = ['bye', 'exit', 'quit']
        msg_type = 'exit' if user_message.lower() in exit_cmds else 'normal'

        return jsonify({
            'response': response,
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': msg_type
        })

    except Exception as e:
        return jsonify({'response': 'Error processing request.', 'type': 'error'}), 500

@app.route('/api/reset', methods=['POST'])
def reset():
    chatbot.reset()
    return jsonify({'message': 'Chat reset', 'status': 'success'})

@app.route('/api/info')
def info():
    return jsonify({
        'project': 'Project 1',
        'phase': 'Foundation',
        'type': 'Deterministic',
        'intents': len(chatbot.responses)
    })

if __name__ == '__main__':
    print("🚀 DecodeLabs | Project 1 - Phase 1: Foundation")
    app.run(debug=True, host='127.0.0.1', port=5000)
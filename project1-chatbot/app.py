"""
DecodeLabs - Project 1
Flask Web Server for Rule-Based AI Chatbot
Serving the Deterministic Logic Engine
"""

from flask import Flask, render_template, request, jsonify, session
from chatbot import RuleBasedChatbot
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'decode-labs-project1-2026'  # For session management

# Initialize the chatbot logic engine (singleton)
# This is our Deterministic System - 100% traceable, 0% hallucination
chatbot = RuleBasedChatbot()

# Store active chatbot instances per session (for multi-user support)
chatbot_instances = {}

def get_chatbot():
    """Get or create chatbot instance for current session"""
    session_id = session.get('session_id')
    if not session_id:
        import uuid
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id

    if session_id not in chatbot_instances:
        chatbot_instances[session_id] = RuleBasedChatbot()

    return chatbot_instances[session_id]


@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint - processes user input through the logic engine

    Input: JSON { "message": "user text" }
    Output: JSON {
        "response": "bot reply",
        "timestamp": "HH:MM:SS",
        "type": "normal|exit|error",
        "interaction_id": "..."
    }
    """
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({
                'response': 'Please provide a message.',
                'timestamp': datetime.now().strftime('%H:%M:%S'),
                'type': 'error'
            }), 400

        user_message = data['message'].strip()

        if not user_message:
            return jsonify({
                'response': 'Please type something! Empty messages cannot be processed.',
                'timestamp': datetime.now().strftime('%H:%M:%S'),
                'type': 'error'
            })

        # Get session-specific chatbot instance
        bot = get_chatbot()

        # Process through the deterministic logic engine
        response = bot.process_input(user_message)

        # Determine message type
        exit_commands = ['bye', 'exit', 'quit', 'goodbye', 'see you later', 'end']
        if user_message.lower() in exit_commands:
            msg_type = 'exit'
        else:
            msg_type = 'normal'

        return jsonify({
            'response': response,
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': msg_type,
            'interaction_number': bot.total_interactions
        })

    except Exception as e:
        print(f"Error processing chat: {e}")
        return jsonify({
            'response': 'I encountered an internal error. Please try again.',
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': 'error'
        }), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    """
    Get conversation history
    Demonstrates WHITE BOX traceability
    Input → Logic → Output - No Mystery
    """
    try:
        bot = get_chatbot()
        history_data = bot.get_history()

        return jsonify({
            'success': True,
            'data': history_data,
            'message': f"Total interactions: {history_data['total']}"
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/reset', methods=['POST'])
def reset_chat():
    """Reset the chatbot conversation"""
    try:
        bot = get_chatbot()
        bot.reset()

        return jsonify({
            'success': True,
            'message': 'Conversation reset successfully. Logic engine ready for new input.',
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/info', methods=['GET'])
def bot_info():
    """Get chatbot system information"""
    return jsonify({
        'name': 'DecodeLabs Rule-Based AI Chatbot',
        'project': 'Project 1 - Industrial Training Kit',
        'batch': '2026',
        'type': 'Deterministic Logic Engine (System 2: The Engineer)',
        'architecture': {
            'pattern': 'Hash Map / Dictionary',
            'complexity': 'O(1) Constant Time',
            'approach': 'Atomic .get() method',
            'anti_pattern_avoided': 'If-Elif Ladder (O(n) Linear)'
        },
        'features': [
            'Input Sanitization (case & whitespace)',
            'Direct Hash Map Access',
            'Fuzzy Keyword Matching',
            'Multi-turn Conversation',
            'Session Management',
            'White Box Traceability',
            'Clean Exit Strategy',
            'Professional Fallback Handling'
        ],
        'model': 'IPO (Input-Process-Output)',
        'intents_count': len(chatbot.responses),
        'status': 'ONLINE',
        'hallucination_risk': '0% (Hard-coded deterministic)',
        'compliance': 'Finance & Healthcare Ready'
    })


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get current chatbot statistics"""
    try:
        bot = get_chatbot()
        stats = bot.get_history()

        return jsonify({
            'success': True,
            'total_interactions': stats['total'],
            'fallback_count': stats['fallbacks'],
            'efficiency': stats['efficiency'],
            'active_sessions': len(chatbot_instances)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'error': 'Endpoint not found',
        'tip': 'Available endpoints: /api/chat, /api/history, /api/reset, /api/info, /api/stats'
    }), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'error': 'Internal server error',
        'message': 'Please try again later'
    }), 500


if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║     DecodeLabs - Project 1                       ║
    ║     Rule-Based AI Chatbot                        ║
    ║                                                  ║
    ║     Architecture: DETERMINISTIC (White Box)      ║
    ║     Pattern: Hash Map / Dictionary               ║
    ║     Complexity: O(1) Constant Time               ║
    ║     Status: 🟢 ONLINE                            ║
    ║                                                  ║
    ║     Access: http://127.0.0.1:5000               ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════════╝
    """)

    app.run(
        debug=True,
        host='127.0.0.1',
        port=5000
    )
"""
DecodeLabs - Project 1: Rule-Based AI Chatbot
Phase 1: Foundation - Core Logic Engine
========================================
Architecture: Hash Map / Dictionary
Complexity: O(1) Constant Time
Model: IPO (Input-Process-Output)
"""

class RuleBasedChatbot:
    """Deterministic Logic Engine - White Box Architecture"""

    def __init__(self):
        # Core Knowledge Base (Phase 1: Essential Intents)
        self.responses = {
            # Greetings
            'hello': 'Hello! Welcome to DecodeLabs. I am your Rule-Based AI Chatbot for Project 1.',
            'hi': 'Hi there! Ready to explore deterministic AI?',
            'hey': 'Hey! Great to have you here. What would you like to learn?',

            # How are you
            'how are you': 'I am running at optimal efficiency! As a deterministic system, I am always consistent.',

            # Capabilities
            'what can you do': 'I can greet you, answer basic questions, tell jokes, and demonstrate rule-based AI.',
            'help': 'Commands: hello, what is AI?, tell me a joke, what is Project 1?, bye',

            # AI Knowledge
            'what is ai': 'AI is the simulation of human intelligence by machines. We are building its foundation with rule-based logic!',
            'what is machine learning': 'ML is a subset of AI where systems learn from data. But first, master deterministic logic!',

            # Project Info
            'what is project 1': 'Project 1 is the Rule-Based AI Chatbot - your foundation at DecodeLabs. Master control flow & if-else logic!',
            'what is decodelabs': 'DecodeLabs forges AI engineers through hands-on projects. You are on Project 1!',

            # Jokes
            'tell me a joke': 'Why do programmers prefer dark mode? Because light attracts bugs! 🐛',
            'another joke': 'What is a computer\'s favorite beat? An algo-rhythm! 🎵',

            # Technical Concepts
            'what is a hash map': 'A Hash Map (Dictionary) provides O(1) lookups. We use it instead of if-elif ladders!',
            'what is deterministic': 'Deterministic means 100% predictable - same input always gives same output. Zero hallucinations!',

            # Gratitude
            'thank you': 'You are welcome! Keep building your AI portfolio.',
            'thanks': 'Happy to help! On to the next milestone!',

            # Exit
            'bye': 'Goodbye! Your deterministic engine is complete. Ready for Phase 2!',
            'exit': 'Exiting. Great work on Project 1 fundamentals!',
            'quit': 'Shutting down. Control flow mastered!',
        }
        self.keyword_map = {
        'hello': 'hello', 'hi': 'hi', 'hey': 'hey',
        'morning': 'hello', 'afternoon': 'hello', 'evening': 'hello',
        'ai': 'what is ai', 'machine learning': 'what is machine learning',
        'ml': 'what is machine learning', 'deep learning': 'what is ai',
        'joke': 'tell me a joke', 'funny': 'tell me a joke',
        'project': 'what is project 1', 'decodelabs': 'what is decodelabs',
        'hash': 'what is a hash map', 'deterministic': 'what is deterministic',
        'sad': 'i am sad', 'confused': 'i am confused', 'stuck': 'i am stuck',
        'thank': 'thank you',
    }

        # Conversation tracking
        self.history = []

    def _fuzzy_match(self, sanitized):
        """Extended keyword matching"""
        for keyword, intent in self.keyword_map.items():
            if keyword in sanitized:
                return self.responses.get(intent)
        return None

    def process_input(self, user_input):
        sanitized = user_input.strip().lower()
        self.history.append({'input': user_input, 'sanitized': sanitized})

        # Exact match first, then fuzzy
        response = self.responses.get(sanitized)
        if response is None:
            response = self._fuzzy_match(sanitized)
        if response is None:
            response = self._get_fallback()

        self.history[-1]['response'] = response

        return response

    def _get_fallback(self):
        return "I don't understand. Try: hello, what is AI?, tell me a joke, help, or bye."

    def get_history(self):
        return {'interactions': self.history, 'total': len(self.history)}

    def reset(self):
        self.history = []

# Singleton instance
chatbot = RuleBasedChatbot()

# Test (only when run directly)
if __name__ == "__main__":
    print("DecodeLabs Logic Engine | Phase 1")
    tests = ["Hello", "What is AI?", "Random", "bye"]
    for t in tests:
        print(f"👤: {t}\n🤖: {chatbot.process_input(t)}\n")
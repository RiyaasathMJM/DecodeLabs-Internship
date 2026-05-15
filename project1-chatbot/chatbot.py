"""
DecodeLabs - Project 1: Rule-Based AI Chatbot
The Logic Engine: Deterministic White-Box Implementation
Follows IPO Model: Input → Process → Output
"""

class RuleBasedChatbot:
    """
    System 2: The Engineer (Deterministic)
    Hash Map Architecture - O(1) lookup time
    No if-elif ladder - Professional approach using dictionaries
    """

    def __init__(self):
        # Knowledge Base using Dictionary (Hash Map)
        # Direct Access instead of Sequential Scan
        self.responses = {
            # === GREETINGS ===
            'hello': 'Hello! Welcome to DecodeLabs. I am your Rule-Based AI Chatbot for Project 1. How can I assist you today?',
            'hi': 'Hi there! Ready to dive into the world of deterministic AI?',
            'hey': 'Hey! Great to have you here. What would you like to learn about?',
            'good morning': 'Good morning! Fresh day to build some AI logic. Ready to code?',
            'good afternoon': 'Good afternoon! Hope your AI journey is going well!',
            'good evening': 'Good evening! Still coding? That is the spirit of an AI engineer!',
            'greetings': 'Greetings, future AI engineer! What brings you here today?',

            # === HOW ARE YOU ===
            'how are you': 'I am running at optimal efficiency! As a deterministic system, I do not have feelings - but my logic engine is 100% functional. How about you?',
            'how are you doing': 'Performing at peak capacity! Zero errors, zero hallucinations. How is your day going?',
            'how do you feel': 'As a rule-based system, I do not feel - I compute! But if I could, I would say I feel very logical today.',

            # === CAPABILITIES ===
            'what can you do': 'I am a Rule-Based AI Chatbot with these capabilities:\n• Greet users intelligently\n• Share AI/ML knowledge\n• Tell programmer jokes\n• Explain Project 1 concepts\n• Demonstrate hash map efficiency\n• Run in a continuous loop (until exit)\n\nTry asking me about AI, Project 1, or just say hello!',
            'help': 'Here is what you can try:\n• "Hello" - Greet me\n• "What is AI?" - Learn about AI\n• "Tell me a joke" - Get a programmer joke\n• "What is Project 1?" - Understand your milestone\n• "What is a hash map?" - Learn professional architecture\n• "bye" - Exit the conversation',

            # === AI KNOWLEDGE ===
            'what is ai': 'Artificial Intelligence (AI) is the simulation of human intelligence by machines. It encompasses:\n• Rule-Based Systems (what we are building now!)\n• Machine Learning\n• Deep Learning\n• Natural Language Processing\n\nRemember: Before you can manage probabilistic AI, master deterministic logic!',
            'what is artificial intelligence': 'AI is the broad field of making machines intelligent. Right now, you are building its foundation - a deterministic rule-based chatbot that operates on explicit if-else logic. This is where every AI engineer starts!',
            'what is machine learning': 'Machine Learning is a subset of AI where systems learn patterns from data instead of following explicit rules. But first, master Project 1 - control flow and deterministic logic. ML comes in Project 2!',
            'what is deep learning': 'Deep Learning uses neural networks with multiple layers. It is powerful but complex. Start with rule-based systems (Project 1), then vector embeddings (Project 2), and eventually you will build neural networks!',
            'what is an llm': 'LLM (Large Language Model) is a probabilistic AI system like GPT. But without rule-based guardrails, it can hallucinate. That is why we build deterministic systems first - they are the skeleton that holds the intelligence!',
            'what is nlp': 'NLP (Natural Language Processing) enables machines to understand human language. Even our simple rule-based bot with input sanitization is a basic form of NLP!',

            # === PROJECT 1 KNOWLEDGE ===
            'what is project 1': 'Project 1 is the Rule-Based AI Chatbot - your foundation milestone at DecodeLabs! Key requirements:\n• Handle greetings and exit commands\n• Use if-else logic (or better: dictionaries!)\n• Run in a continuous loop\n• Input sanitization\n• Fallback for unknown inputs\n\nMaster this, and you unlock all other projects!',
            'tell me about project 1': 'Project 1: Rule-Based AI Chatbot is your first step as an AI Engineer at DecodeLabs. You build a deterministic chatbot using:\n• Hash Maps (not if-elif ladders!)\n• IPO Model architecture\n• The .get() method for atomic lookups\n• Continuous while loop\n\nThis proves you can simulate human interaction through pure programmatic decision-making.',
            'what is decodelabs': 'DecodeLabs is where AI engineers are forged! Industry training with hands-on projects:\n• Project 1: Rule-Based Chatbot (you are here!)\n• More projects unlocked after completion\n• Real-world portfolio building\n• From deterministic logic to generative AI',

            # === HASH MAP CONCEPTS ===
            'what is a hash map': 'A Hash Map (Dictionary in Python) is the PROFESSIONAL approach for our chatbot:\n\n❌ ANTI-PATTERN (If-Elif Ladder):\n  O(n) complexity, high technical debt\n\n✅ PROFESSIONAL (Hash Map):\n  O(1) direct access, clean, maintainable\n\nWe use: responses.get(user_input, fallback)',
            'what is o(1)': 'O(1) means constant time complexity - the holy grail of algorithms! With our hash map/dictionary, response lookup takes the same time regardless of how many intents we have. Compare this to an if-elif ladder which is O(n) - it gets slower with each new condition.',
            'what is deterministic': 'Deterministic means 100% predictable - same input always gives same output. Our rule-based bot is a "White Box" - you can trace Input → Logic → Output with zero mystery. No hallucinations, no randomness, just pure hard-coded logic!',

            # === IPO MODEL ===
            'what is the ipo model': 'IPO Model = Input → Process → Output\n\nOur chatbot follows this exactly:\n📥 INPUT: User types message → sanitization (lowercase, strip)\n⚙️ PROCESS: Hash map lookup with .get() method\n📤 OUTPUT: Deterministic response or fallback\n\nThis is the blueprint of our logic engine!',

            # === JOKES ===
            'tell me a joke': 'Why do programmers prefer dark mode?\n\nBecause light attracts bugs! 🐛😄',
            'another joke': 'What is a computer\'s favorite beat?\n\nAn algo-rhythm! 🎵',
            'tell me another joke': 'Why did the Python programmer not get off the roller coaster?\n\nBecause they were stuck in an infinite loop! 🔄',
            'more jokes': 'How many programmers does it take to change a light bulb?\n\nNone - that is a hardware problem! 💡',
            'joke': 'Why was the JavaScript developer sad?\n\nBecause they did not know how to "null" their feelings! 😢',

            # === ENCOURAGEMENT ===
            'i am confused': 'That is completely normal! AI is a vast field. Start with the basics:\n1. Understand control flow (if-else)\n2. Master data structures (dictionaries)\n3. Build deterministic systems (this project!)\n4. Then move to ML/DL\n\nYou are on the right track!',
            'i am stuck': 'Do not give up! Every AI engineer faces challenges. Remember:\n• Break down the problem\n• Check your logic flowchart\n• Use print statements for debugging\n• The solution is often simpler than you think\n\nYou have got this! 💪',
            'i am sad': 'Hey, cheer up! You are building AI systems - that is amazing! Even the best engineers started with "Hello World". Your first chatbot is a huge achievement. Keep going!',
            'motivate me': '🔥 MOTIVATION MODE ACTIVATED 🔥\n\n"The absolute best way to master AI is through hands-on practice, not just theory."\n\nYou are not just learning - you are BUILDING. Every line of code is one step closer to becoming a professional AI engineer. Now go crush Project 1!',

            # === GRATITUDE ===
            'thank you': 'You are welcome! Remember: Practice beats theory. Keep building!',
            'thanks': 'Happy to help! Your AI journey is just beginning. On to Project 2 after this!',
            'great': 'Glad I could help! Your deterministic logic engine is shaping up nicely.',
            'awesome': 'You are awesome too! Keep that enthusiasm - it will take you far in AI.',
            'cool': 'Right? Rule-based systems are cool when built professionally! Wait until you see what Projects 2, 3, and beyond have in store.',

            # === EXIT COMMANDS ===
            'bye': 'Goodbye! Your logic engine is complete. Ready for Project 2: Vector Embeddings? See you next time at DecodeLabs!',
            'exit': 'Exiting the deterministic engine. Great work on Project 1! Your portfolio just got stronger.',
            'quit': 'Shutting down... Remember: Control flow mastery is the foundation of all AI. See you soon!',
            'goodbye': 'Goodbye, future AI engineer! Keep building, keep learning, and never stop coding.',
            'see you later': 'See you later! The rule-based skeleton is built. Next stop: teaching machines to learn!',
            'end': 'Conversation ended. Your Project 1 chatbot performed flawlessly. Time to tackle the next challenge!',
        }

        # Extended fuzzy matching keywords
        self.keyword_map = {
            'hello': 'hello', 'hi': 'hi', 'hey': 'hey', 'morning': 'good morning',
            'afternoon': 'good afternoon', 'evening': 'good evening',
            'joke': 'tell me a joke', 'funny': 'tell me a joke',
            'ai': 'what is ai', 'artificial intelligence': 'what is artificial intelligence',
            'machine learning': 'what is machine learning', 'ml': 'what is machine learning',
            'deep learning': 'what is deep learning', 'dl': 'what is deep learning',
            'llm': 'what is an llm', 'nlp': 'what is nlp',
            'project': 'what is project 1', 'decodelabs': 'what is decodelabs',
            'hash map': 'what is a hash map', 'hashmap': 'what is a hash map',
            'dictionary': 'what is a hash map', 'o(1)': 'what is o(1)',
            'deterministic': 'what is deterministic', 'ipo': 'what is the ipo model',
            'help': 'help', 'capable': 'what can you do', 'can you do': 'what can you do',
            'thank': 'thank you', 'thanks': 'thanks',
            'sad': 'i am sad', 'confused': 'i am confused', 'stuck': 'i am stuck',
            'motivate': 'motivate me', 'encourage': 'motivate me',
            'bye': 'bye', 'exit': 'exit', 'quit': 'quit', 'goodbye': 'goodbye',
            'how are you': 'how are you', 'feel': 'how do you feel',
        }

        # Conversation history for White Box traceability
        self.history = []

        # Session statistics
        self.total_interactions = 0
        self.fallback_count = 0

    def process_input(self, user_input):
        """
        PHASE 1: INPUT SANITIZATION
        PHASE 2: HASH MAP LOOKUP (Atomic Operation)
        PHASE 3: FALLBACK HANDLING
        """
        # PHASE 1: Sanitize input
        sanitized = user_input.strip().lower()

        # Log the interaction
        self.history.append({
            'input_raw': user_input,
            'input_sanitized': sanitized
        })
        self.total_interactions += 1

        # PHASE 2: Atomic lookup + fallback
        # This is the PROFESSIONAL approach - single line, O(1) complexity
        response = self.responses.get(sanitized)

        # PHASE 3: If no exact match, try fuzzy keyword matching
        if response is None:
            response = self._fuzzy_match(sanitized)
            self.fallback_count += 1

        # Log response
        self.history[-1]['response'] = response

        return response

    def _fuzzy_match(self, sanitized_input):
        """
        Extended matching using keyword detection
        Still efficient - checks keywords and returns early
        """
        # Check for partial keyword matches
        for keyword, intent in self.keyword_map.items():
            if keyword in sanitized_input:
                return self.responses.get(intent, self._get_fallback())

        return self._get_fallback()

    def _get_fallback(self):
        """Default response for completely unknown inputs"""
        fallbacks = [
            "I do not understand that yet. I am a rule-based system with specific intents. Try asking:\n• About AI / Machine Learning\n• For a joke\n• About Project 1\n• Just say 'hello' or 'help'",
            "That is beyond my deterministic rules. I excel at:\n👋 Greetings\n🤖 AI concepts\n😄 Programmer jokes\n📚 Project 1 knowledge\n\nTry one of these topics!",
            "Unknown input detected. Remember: I am a White Box system - I only respond to programmed intents. Type 'help' to see what I can do!"
        ]
        # Cycle through fallbacks based on interaction count
        return fallbacks[self.total_interactions % len(fallbacks)]

    def get_history(self):
        """Return complete conversation history (White Box traceability)"""
        return {
            'interactions': self.history,
            'total': self.total_interactions,
            'fallbacks': self.fallback_count,
            'efficiency': f"{((self.total_interactions - self.fallback_count) / max(1, self.total_interactions) * 100):.1f}%"
        }

    def reset(self):
        """Reset chatbot state"""
        self.history = []
        self.total_interactions = 0
        self.fallback_count = 0


# Create singleton instance
chatbot = RuleBasedChatbot()

# Test the engine if run directly
if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════╗
    ║  DecodeLabs - Logic Engine Test ║
    ╚══════════════════════════════════╝
    """)

    test_inputs = ["Hello", "What is AI?", "Tell me a joke", "random text", "bye"]

    for test_input in test_inputs:
        response = chatbot.process_input(test_input)
        print(f"\n👤 User: {test_input}")
        print(f"🤖 Bot: {response}")
        print("-" * 40)

    print("\n📊 Chatbot Statistics:")
    print(chatbot.get_history())
class ChatBot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey"]
        self.farewells = ["bye", "goodbye", "see you later"]
        self.default_response = "I'm sorry, I don't understand that."

    def respond_to_message(self, message):
        message = message.lower()
        if any(greet in message for greet in self.greetings):
            return "Hello! How can I assist you today?"
        elif any(farewell in message for farewell in self.farewells):
            return "Goodbye! Have a great day!"
        else:
            return self.default_response
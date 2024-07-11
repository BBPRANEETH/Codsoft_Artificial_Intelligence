responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi! How can I assist you?",
    "what is your name": "I'm a language model created by AI technology. You can think of me as a digital assistant here to help with information, answer questions, or just chat. How can I assist you today?",
    "how are you": "I'm good, thank you!",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! How can I assist you today?",
    "good evening": "Good evening! How can I assist you today?",
    "have a good day": "Thank you! Wishing you a wonderful day ahead as well! If you have any questions or need assistance, feel free to ask.",
    "see you later": "See you later! Have a great day.",
    "what is the weather report": "The weather in Hyderabad, India is currently 28 degrees Celsius and cloudy.",
    "how do i use you": "To use me, simply type a question or request and I will do my best to respond.",
    "how much do you cost": "I am currently free to use.",
    "what are your features": "I can generate text, translate languages, conversation,coding assistance and answering the questions in interactive way",
    "what is the news today": "Here is the summary of the top news of today...",
    "i would like to book a appointment with dr.baali": "Sure, what date and time would you like to book your appointment for?",
    "bye": "Goodbye! Have a nice day.",
    "default": "I'm sorry, I don't understand that. Please ask me something else."
}

def respond(input_text):
    input_text = input_text.lower()
    if input_text in responses:
        return responses[input_text]
    else:
        return responses["default"]

def main():
    print("Welcome! Ask me anything or say 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(respond(user_input))
            break
        else:
            print("Bot:", respond(user_input))

if __name__ == "__main__":
    main()

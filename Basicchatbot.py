def chatbot_reply(message):
    message = message.lower()   # Convert to lowercase for easy matching

    if "hello" in message or "hi" in message:
        return "Hi! How can I help you?"
    elif "how are you" in message:
        return "I'm fine, thanks! How are you?"
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."

# Main chatbot loop
print("Chatbot activated! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    reply = chatbot_reply(user_input)
    print("Bot:", reply)

    if "bye" in user_input.lower():
        break

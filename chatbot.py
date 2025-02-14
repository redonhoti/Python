
def chatbot():
    print("Chatbot: Hi, I'm your chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "weather" in user_input:
            print("Chatbot: Sorry, I can't fetch the weather right now.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I didn't understand that.")

chatbot()

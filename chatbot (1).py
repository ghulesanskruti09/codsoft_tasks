def chatbot():
    print("================================")
    print("      RULE-BASED CHATBOT")
    print("================================")
    print("Chatbot: Hello! I am your chatbot.")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif "your name" in user or "who are you" in user:
            print("Chatbot: I am a simple rule-based chatbot.")

        elif "how are you" in user:
            print("Chatbot: I am doing great! Thank you.")

        elif "help" in user:
            print("Chatbot: I can answer simple predefined questions.")

        elif "thank" in user:
            print("Chatbot: You're welcome!")

        elif user in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
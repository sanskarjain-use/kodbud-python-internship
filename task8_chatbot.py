"""Task 8: Simple Rule-Based CLI Chatbot"""


def reply(msg):
    m = msg.lower().strip()
    words = m.replace("!", " ").replace("?", " ").replace(",", " ").split()
    if any(w in words for w in ("hello", "hi", "hey")):
        return "Hello! How can I help you today?"
    elif "how are you" in m:
        return "I'm just a bot, but I'm doing great. Thanks for asking!"
    elif "your name" in m:
        return "I'm KodBot, a simple Python chatbot."
    elif "internship" in m:
        return "Kodbud's Python internship has 8 tasks; complete any 4."
    elif "python" in m:
        return "Python is a versatile, beginner-friendly programming language."
    elif "help" in m:
        return "Try: hello, how are you, your name, internship, python, bye."
    elif m in ("bye", "exit", "quit"):
        return "Goodbye! Have a great day."
    return "Sorry, I didn't understand that. Type 'help' for options."


def main():
    print("KodBot: Hi! Type 'bye' to exit.")
    while True:
        text = input("You: ")
        answer = reply(text)
        print("KodBot:", answer)
        if text.lower().strip() in ("bye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()

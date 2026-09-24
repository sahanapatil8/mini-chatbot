from datetime import datetime


def calculator():
    try:
        number1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        number2 = float(input("Enter second number: "))

        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*":
            result = number1 * number2
        elif operator == "/":
            if number2 == 0:
                return "Cannot divide by zero."
            result = number1 / number2
        else:
            return "Invalid operator."

        return f"The answer is {result}"


    except ValueError:
        return "Please enter valid numbers."


def chatbot_response(message, name):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif "your name" in message:
        return "My name is MiniBot."

    elif "how are you" in message:
        return "I am doing great! Thanks for asking."

    elif "python" in message:
        return "Python is a popular programming language."

    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in message:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    elif "who are you" in message:
        return "I am MiniBot, a simple Python chatbot."

    elif "thank" in message:
        return "You're welcome!"

    elif "calculate" in message:
        return calculator()

    elif "good" in message:
        return "That's great to hear!"

    elif "bad" in message:
        return "I'm sorry to hear that. I hope your day gets better!"

    else:
        return "Sorry, I don't understand that yet."


def main():
    print("================================")
    print("        🤖 MINIBOT")
    print("================================")
    print("Hello! I am MiniBot.")
    print("Type 'bye' to exit.")
    print()

    name = input("What is your name? ")

    print(f"Nice to meet you, {name}!")
    print()

    while True:
        message = input("You: ")

        if message.lower().strip() in ["bye", "exit", "quit"]:
            print(f"MiniBot: Goodbye, {name}! Have a great day.")
            break

        response = chatbot_response(message, name)
        print("MiniBot:", response)


if __name__ == "__main__":
    main()

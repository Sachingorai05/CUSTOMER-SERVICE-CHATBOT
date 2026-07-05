import json
from datetime import datetime

with open("intents.json", "r") as file:
    intents = json.load(file)

print("=" * 50)
print("🤖 CUSTOMER SERVICE CHATBOT")
print("Type 'exit' to quit the chatbot.")
print("=" * 50)

while True:
    user_message = input("\nYou: ").lower()

    if user_message == "exit":
        print("Bot: Thank you for contacting us. Goodbye!")
        break

    response = "Sorry, I didn't understand your query. Please try again."

    response = "Sorry, I didn't understand your query. Please contact support@example.com."

for intent, data in intents.items():
    if any(keyword in user_message for keyword in data["keywords"]):
        response = data["response"]
        break

    print("Bot:", response)

    with open("chat_history.txt", "a") as log:
        log.write(
            f"{datetime.now()} | User: {user_message} | Bot: {response}\n"
        )
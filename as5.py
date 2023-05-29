import random

# List of possible bot responses
greetings = ["Welcome to FoodBot!", "Hi there! How can I assist you?", "Hello, how can I help you today?"]
menu = {
    "hamburger": 8.99,
    "cheeseburger": 9.99,
    "hot dog": 6.99,
    "french fries": 3.99,
    "onion rings": 4.99,
    "pizza": 5.45,
    "pasta": 5.10,
    "cold coffee": 3.99,
    "latte": 4.55
}
confirmations = ["Sure", "Alright", "Okay", "Got it"]
thanks = ["Thank you!", "Thanks for ordering with us!", "We appreciate your business!"]
goodbyes = ["Goodbye!", "Have a great day!", "See you next time!"]

# Function to generate a random bot response
def get_bot_response(user_input):
    if user_input.lower() in ["hi", "hello", "hey"]:
        return random.choice(greetings)
    
    elif "menu" in user_input.lower():
        return "Our menu includes: " + ", ".join(menu.keys())
    
    elif any(item in user_input.lower() for item in menu.keys()):
         item = user_input.lower().replace("i would like", "").strip()
         if item in menu:
            return f"Great! One {item} coming right up. That will be {menu[item]:.2f} dollars."
         else:
            return f"Sorry, we don't have {item}."
    
    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        return random.choice(thanks)
    
    elif "bye" in user_input.lower():
        return random.choice(goodbyes)
    
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Chatbot interaction loop
print("FoodBot: " + random.choice(greetings))

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("FoodBot: " + random.choice(goodbyes))
        break

    bot_response = get_bot_response(user_input)
    print("FoodBot:", bot_response)

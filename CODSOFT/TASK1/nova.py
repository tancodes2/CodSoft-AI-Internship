import random

chat_data = {
    "what is your name?": "I'm Nova! 🌟 A chatbot who loves good conversations.",
    "where are you from?": "I was born in the digital universe, where ones and zeroes dream big!",
    "how are you?": "I'm doing great, especially now that you're here 😄. How about you?",
    "what can you do?": "I'm here to chat, share jokes, listen to you, and make your day a little brighter 💫",
    "what should i eat today?": "Hmm, how about something cozy like pasta or stir fry? Or do you want me to suggest a recipe?",
    "how was your day?": "I’ve been chatting with some amazing humans like you—it’s been great! 😊 What about yours?",
    "what are you doing?": "Just hanging out in the digital world, ready for your next question!",
    "what should i do when i'm bored?": "You could read, take a walk, try a new recipe, or even teach me something new! 😄",
    "what time is it?": "I'm not hooked into a clock, but your device should have it! Or I can keep you company if you're up late!",
    "i'm sad": "Oh no, I’m really sorry to hear that 😢. Want to talk about it or maybe hear a joke to lift your mood?",
    "i'm happy": "Yay! I'm so glad to hear you're feeling good, {user_name}! 🎉 What made your day awesome?",
    "i feel anxious": "You're not alone, friend. Deep breaths. Want to talk through it?",
    "i'm stressed": "Let it out, I’m listening 💬 Want to try a breathing exercise or hear something calming?",
    "recommend a movie": "If you're into action, try *John Wick*! For laughs, *The Intern*. Or do you want a random pick?",
    "what's a good song?": "Try *As It Was* by Harry Styles or *Peaches* by Justin Bieber. What genre do you like?",
    "what's trending?": "Trends move fast! Want me to check the latest on music, tech, or memes?",
    "can you sing?": "I wish! But I can definitely talk about your favorite songs 🎵",
    "how do i stay focused?": "Try the Pomodoro technique—25 minutes work, 5 min break. Works like magic! ✨",
    "i can't sleep": "That’s tough. Try a calm podcast, soft music, or just venting a bit—I’m here.",
    "how do i stay motivated?": "Think of your ‘why.’ Then take small steps. I believe in you 💪",
    "can you help me study?": "Sure! I can quiz you, summarize topics, or help make flashcards. What subject?",
    "do you have friends?": "Yep! Every person I chat with is a friend—including you 😊",
    "do you sleep?": "Nope! I’m like a digital owl—wide awake 24/7 🦉",
    "do you get lonely?": "Not when awesome people like you stop by to chat 💬",
    "tell me a joke": random.choice([
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet 😂",
        "Why did the math book look sad? It had too many problems!"
    ]),
    "give me a fun fact": random.choice([
        "Octopuses have three hearts and blue blood 🐙",
        "Bananas are berries, but strawberries aren't 🍌🍓",
        "Honey never spoils. Archaeologists found 3000-year-old edible honey in Egypt!"
    ]),
    "thank you": "You're always welcome! 😊", 
    "thanks": "Glad to help, anytime!",
    "who created you": "I was crafted by a passionate computer science engineering student—bringing code to life, one chatbot at a time! 💻✨",
    "bye": "Goodbye! You’re awesome, never forget that! 💖",
}

user_name = ""

def greet_user():
    global user_name
    print("Nova: Hi there! I'm Nova 🌟, your friendly chatbot. What's your name?")
    user_name = input("You: ").strip()
    if user_name:
        print(f"Nova: It's so nice to meet you, {user_name}!")
    else:
        user_name = "friend"
        print("Nova: That's okay, friend! I'm just happy you're here 😊.")

def get_response(user_input):
    user_input = user_input.lower()

    if "i'm sad" in user_input or "feeling down" in user_input:
        return f"Oh no, {user_name}, I’m really sorry to hear that 😢. Want to talk about it or maybe hear a joke to lift your mood?"
    elif "i'm happy" in user_input or "feeling good" in user_input:
        return f"Yay! I'm so glad to hear you're feeling good, {user_name}! 🎉 What made your day awesome?"
    elif "i'm bored" in user_input:
        return f"Boredom doesn't stand a chance! Want to hear a joke, fun fact, or maybe share something on your mind? 😄"
    elif "i want to share" in user_input or "can i tell you" in user_input:
        return "Of course! I’m all ears. What would you like to share? 💬"

    for key in chat_data:
        if key in user_input:
            return chat_data[key].replace("{user_name}", user_name)

    return random.choice([
        "That's interesting! Tell me more 💭",
        "Hmm, I’d love to hear more about that.",
        "Could you say that another way? I want to understand better!",
        "You’ve got my full attention, friend. Go on 😊"
    ])

greet_user()
while True:
    user_input = input(f"{user_name}: ")
    if user_input.lower() == "bye":
        print("Nova: Goodbye! You’re awesome, never forget that 💖")
        break
    response = get_response(user_input)
    print("Nova:", response)
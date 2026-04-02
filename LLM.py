import random

def get_llm_response(user_input):
    user_lower = user_input.lower()
    
    responses = {
        "hello": [
            "Hello! How are you feeling today?",
            "Hi there! How can I assist you?",
            "Greetings! What's on your mind?"
        ],
        "my name is": [
            f"Nice to meet you! Tell me more about yourself.",
            f"Hello! It's great to meet you."
        ],
        "stressed": [
            "I understand stress can be overwhelming. Would you like to discuss what's causing your stress?",
            "Feeling stressed is common. Let's talk about what might help you feel better."
        ],
        "tired": [
            "Getting proper rest is important. What's preventing you from sleeping well?",
            "Fatigue can affect many aspects of life. How long have you been feeling tired?"
        ],
        "exams": [
            "Exams can be challenging. Have you tried breaking your study sessions into smaller chunks?",
            "Many students feel pressure during exam time. What subjects are most difficult for you?"
        ],
        "mother": [
            "Family relationships can be complex. Would you like to talk more about your relationship with your mother?",
            "I hear that your mother is strict. How does that make you feel?"
        ],
        "sleep": [
            "Sleep is essential for mental health. What time do you usually go to bed?",
            "Not getting enough sleep can increase stress. Have you tried establishing a bedtime routine?"
        ]
    }
    
    
    for key, response_list in responses.items():
        if key in user_lower:
            return random.choice(response_list)
    
    defaults = [
        "That's interesting. Can you tell me more?",
        "I see. How does that make you feel?",
        "Please continue sharing your thoughts.",
        "What else is on your mind?"
    ]
    
    return random.choice(defaults)

if __name__ == "__main__":
    print("="*60)
    print("MODERN AI CHATBOT")
    print("="*60)
    print("Type 'quit' to stop\n")
    
    test_prompts = [
        "Hello",
        "My name is David",
        "I feel stressed",
        "I am tired",
        "Because I have exams",
        "My mother is strict",
        "I need more sleep"
    ]
    
    for prompt in test_prompts:
        print(f"You: {prompt}")
        print(f"Bot: {get_llm_response(prompt)}\n")
    
    print("-"*40)
    print("Interactive mode:\n")
    
    while True:
        user = input("You: ").strip()
        if user.lower() == "quit":
            print("Bot: Goodbye! Take care!")
            break
        print(f"Bot: {get_llm_response(user)}\n")
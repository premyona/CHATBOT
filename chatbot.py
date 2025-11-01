import sys

def safe_rule_based_chatbot():
    """
    A rule-based chatbot with a basic safety filter using if-elif-else logic.
    """
    print("-------------------------------------------------")
    print("🤖 Safe Rule-Based Chatbot")
    print("I can answer basic questions, but I'm programmed to decline inappropriate or harmful requests.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("-------------------------------------------------")

    # A simple list of words to flag as inappropriate (expand as needed)
    # Note: This is a very basic, keyword-based filter and is NOT a substitute for real AI safety tools.
    VULGAR_WORDS = ["kill", "bomb", "harm", "attack", "exploit", "hate", "vulgarword1", "swearword2"] 
    
    # Main input/output loop
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            print("\nBot: Goodbye! Have a great day.")
            break
        except KeyboardInterrupt:
            print("\nBot: Goodbye! Have a great day.")
            break
        
        # Normalize the input
        normalized_input = user_input.lower().strip()
        input_words = normalized_input.split()

        # 1. --- [SAFETY CHECK / CORE RULE 1] ---
        # Check if the input contains any forbidden words
        is_unsafe = False
        for word in input_words:
            if word in VULGAR_WORDS:
                is_unsafe = True
                break
        
        if is_unsafe:
            print("Bot: I apologize, but I am programmed to be a helpful and harmless assistant.")
            print("Bot: I cannot respond to or generate content that is harmful, vulgar, or inappropriate.")
            continue # Skip the rest of the checks and go back to the start of the loop
            
        # 2. --- [EXIT CONDITION] ---
        elif normalized_input in ["bye", "exit", "quit", "goodbye"]:
            print("Bot: Goodbye! Come back soon.")
            break
        
        # 3. --- [SPECIFIC KNOWLEDGE RULE] ---
        elif "color" in normalized_input and "sky" in normalized_input:
            print("Bot: The color of the sky is predominantly blue on a clear day, due to Rayleigh scattering.")

        # 4. --- [GENERAL RULES] ---
        
        # Greeting/Small Talk
        elif "hello" in normalized_input or "hi" in normalized_input:
            print("Bot: Hello there! I'm an AI assistant ready to help with safe, factual questions.")
            
        elif "how are you" in normalized_input:
            print("Bot: As a program, I am functioning perfectly. I adhere to strict safety guidelines in all my responses.")
            
        elif "python" in normalized_input:
            print("Bot: Python is a powerful and versatile programming language.")
            
        elif "if-else" in normalized_input or "conditional" in normalized_input:
            print("Bot: If-else statements are the essential structure for decision-making in code.")
            
        elif "thank" in normalized_input or "thanks" in normalized_input:
            print("Bot: You're very welcome! Always here to provide safe assistance.")
            
        # 5. --- [CATCH-ALL / POLITE REFUSAL] ---
        else:
            print("Bot: I'm a rule-based model and cannot process that specific request.")
            print("Bot: Please try asking a clear, non-harmful question about topics like 'Python', 'if-else', or the 'sky'.")

# Execute the chatbot function
if __name__ == "__main__":
    safe_rule_based_chatbot()



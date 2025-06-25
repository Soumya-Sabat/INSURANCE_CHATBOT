from domain_utils import get_domain_answer
import json

def career_chatbot():
    print("\n Career Guidance Chatbot Activated!")
    print("Available domains: data science, blockchain, cybersecurity, web developer, android developer")
    print("Type 'back' to return to the Insurance Chatbot.\n")

    domain = input("Select your domain: ").strip().lower().replace(" ", "_")

    while True:
        user_input = input(" You: ")
        if user_input.lower() in ["back", "exit"]:
            print("Returning to Insurance Chatbot...\n")
            break

        answer = get_domain_answer(domain, user_input)
        print("CareerBot:", answer)

if __name__ == "__main__":
    career_chatbot()

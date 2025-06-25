import json
import subprocess
import re
from utils import calculate_quote, save_claim, save_chat, save_user_policy, get_user_policies

with open("intents.json", "r") as file:
    intents = json.load(file)

def match_intent(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if re.search(r'\b' + re.escape(pattern.lower()) + r'\b', user_input):
                return intent["tag"], intent["responses"]
    return None, None

def chat():
    print("InsBOT: Hello! I support Life, Health, Vehicle, Travel & Property insurance.")
    print('For the career guidance bot , type "career" in the message box to activate ')
    print("Type 'exit' to quit.\n")
    

    expecting_quote = False
    expecting_claim = False
    user_name = "default_user"

    while True:
        user_input = input("You: ")
        save_chat(user_input, sender="user")
        

        if user_input.lower() == "exit":
            response = "Thanks for chatting. Stay insured!"
            print("InsBOT:", response)
            save_chat(response, sender="bot")
            break
        
        if user_input.lower() == "career":
            subprocess.run(["python", "career_main.py"])
            continue


        if expecting_quote:
            try:
                parts = user_input.split()
                age = int(parts[0])
                insurance_type = parts[1].lower()
                premium = calculate_quote(age, insurance_type)
                policy_number = f"{insurance_type[:1].upper()}{100000 + premium}"
                save_user_policy(user_name, insurance_type, policy_number, premium)
                response = f"Estimated premium for {insurance_type} is ₹{premium}/year. Policy number: {policy_number}"
            except:
                response = "Please input like: 30 health"
            print("InsBOT:", response)
            save_chat(response, sender="bot")
            expecting_quote = False
            continue

        if expecting_claim:
            try:
                parts = user_input.split()
                insurance_type = parts[0].lower()
                policy_number = parts[1]
                description = " ".join(parts[2:])
                save_claim(insurance_type, policy_number, description)
                response = f"Claim for policy {policy_number} ({insurance_type}) filed successfully."
            except:
                response = "Please input like: vehicle V998877 minor accident in Delhi"
            print("InsBOT:", response)
            save_chat(response, sender="bot")
            expecting_claim = False
            continue

        tag, responses = match_intent(user_input)
        if tag:
            response = responses[0]
            print("InsBOT:", response)
            save_chat(response, sender="bot")

            if tag == "get_quote":
                expecting_quote = True
            elif tag == "file_claim":
                expecting_claim = True
        elif "my policies" in user_input.lower():
            policies = get_user_policies(user_name)
            if policies:
                formatted = "\n".join([f"- {k.title()} | No: {v['policy_number']} | ₹{v['premium']} | Status: {v['status']}" for k,v in policies.items()])
                response = f"📄 Your active policies:\n{formatted}"
            else:
                response = "No policies found yet."
            print("InsBOT:", response)
            save_chat(response, sender="bot")
        else:
            response = "I'm not sure how to help. Try 'quote', 'file a claim', or 'my policies'."
            print("InsBOT:", response)
            save_chat(response, sender="bot")

if __name__ == "__main__":
    chat()

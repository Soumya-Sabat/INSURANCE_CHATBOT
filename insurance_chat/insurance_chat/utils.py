import json
import os
from datetime import datetime

def calculate_quote(age, insurance_type):
    base = 500
    modifiers = {
        "health": 300,
        "vehicle": 200,
        "life": 400,
        "travel": 250,
        "property": 350
    }
    base += modifiers.get(insurance_type, 0)

    if age > 50:
        base += 200
    elif age < 25:
        base += 150

    return base

def save_claim(policy_type, policy_number, description):
    data = {
        "policy_type": policy_type,
        "policy_number": policy_number,
        "description": description,
        "filed_at": str(datetime.now())
    }
    with open("claims.json", "a") as f:
        f.write(json.dumps(data) + "\n")

def save_chat(message, sender="user"):
    log = {"sender": sender, "message": message, "timestamp": str(datetime.now())}
    chat_file = "chat_history.json"

    if not os.path.exists(chat_file):
        with open(chat_file, "w") as f:
            json.dump([log], f, indent=4)
    else:
        with open(chat_file, "r+") as f:
            history = json.load(f)
            history.append(log)
            f.seek(0)
            json.dump(history, f, indent=4)

def save_user_policy(user="default_user", insurance_type=None, policy_number=None, premium=None):
    file = "policies.json"
    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = {"users": {}}
    
    user_data = data["users"].get(user, {"policies": {}})
    user_data["policies"][insurance_type] = {
        "policy_number": policy_number,
        "premium": premium,
        "status": "active"
    }
    data["users"][user] = user_data
    
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def get_user_policies(user="default_user"):
    with open("policies.json", "r") as f:
        data = json.load(f)
    return data["users"].get(user, {}).get("policies", {})

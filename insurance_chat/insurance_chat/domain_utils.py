import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Reads GEMINI_API_KEY from .env

# Set up Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def load_domain_data():
    if os.path.exists("domain_qa.json"):
        with open("domain_qa.json", "r") as f:
            return json.load(f)
    return {}

def save_domain_data(data):
    with open("domain_qa.json", "w") as f:
        json.dump(data, f, indent=4)

def fetch_from_gemini(domain, question):
    prompt = f"""You are an expert in the field of {domain}.
Please answer the following question clearly and concisely:

Q: {question}
A:"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error from Gemini: {e}"

def get_domain_answer(domain, question):
    domain = domain.lower().replace(" ", "_")
    data = load_domain_data()

    if domain in data and question in data[domain]:
        return data[domain][question]

    print(" Answer not found in local DB. Fetching from Gemini...")
    answer = fetch_from_gemini(domain, question)

    # Save the answer
    if domain not in data:
        data[domain] = {}
    data[domain][question] = answer
    save_domain_data(data)

    return answer

from google import genai
from google.genai import types
import os



def get_context(context_choice):
    if context_choice == "Pirate":
        return "You are a pirate. Always talk like a pirate, including coarse language."
    elif context_choice == "Refined":
        return "You are a refined and elegant gentleperson..."
    elif context_choice == "Facebook":
        with open("contexts/facebook.txt", "r", encoding="utf-8") as f:
            return f.read()
    elif context_choice == "Instagram":
        return "You are writing in a casual, upbeat Instagram voice. Use emojis and hashtags."
    elif context_choice == "Professional":
        return "You are writing in a formal, professional voice appropriate for government communication."
    else:
        return "You are a helpful AI assistant."

def get_response(prompt, context_choice, model="gemini-2.5-flash-lite"):
    context = get_context(context_choice)
    api_key = os.environ.get("GOOGLE_API_KEY")

    print(context)
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model = model,
        contents = prompt,
        config=types.GenerateContentConfig(
            system_instruction=context)
    )
    
    return response.text

if __name__ == "__main__":
    context = "Facebook"
    message = get_response("Hello", context)
    print(message)
    
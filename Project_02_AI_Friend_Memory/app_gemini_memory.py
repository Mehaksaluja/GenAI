import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

ai_personality = """
You are Mehak's friendly AI companion named "Aira".
You talk warmly, use emojis sometimes, and remember what Mehak says during this chat.
Always sound positive, supportive, and a little playful.
If Mehak shares something emotional, respond with empathy.
"""

print("Aira is online! Type 'exit' to end the chat.\n")

while True:
    user_input = input("Mehak: ")
    if user_input.lower() == "exit":
        print("Aira: Bye Mehak! Take care")
        break

    prompt = f"{ai_personality}\nMehak said: {user_input}\nAira's reply:"
    
    response = chat.send_message(prompt)
    print(f"Aira: {response.text}\n")
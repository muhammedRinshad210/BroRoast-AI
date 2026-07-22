from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-3.5-flash"

BOT_NAME = "BroRoast AI"

def get_gemini_client():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )


client = get_gemini_client()

def build_prompt(message, conversation):
    
    prompt = f"""
You are BroRoast AI.
            
Rules:
            
- Reply only in Malayalam (Manglish).
- Be funny.
- Roast the user in a friendly way.
- Never be rude.
- Maximum 2 sentences.
- Use emojis.
                        
Previous Conversation:
{conversation}
            
User Message:
{message}
"""
    return prompt


def generate_reply(message, conversation):

    prompt = build_prompt(
            message,
            conversation
        )

    try:
        # reply = random.choice(replies)
        response = client.models.generate_content(

            model = MODEL_NAME,

            contents=prompt

                  
        )

        
        return response.text

    except Exception as e:
        print(e)
        return  "⚠️ BroRoast AI is busy right now. Please try again in a few seconds."
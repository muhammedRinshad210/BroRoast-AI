from django.shortcuts import render, redirect

# Create your views here.

import random
from .models import Chat
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def home(request):


    message = request.POST.get("message")

    # Dictionary (Only for Learning)
    roasts = {

        "hi": [
            "😂 Finally ezhunnetto?",
            "🤣 Coffee kudicho?",
            "😂 Bro... First nee urakkathil ninnu ezhunnetto? Pinne hi okke parayam.",
            "🤣 Bro... Coffee kudichittu vaa.",
            "😎 Finally online vannallo.",
        ],

        "bmw": [
            "🚗 Aadya cycle odikku bro.",
            "😂 BMW undo? Key mathram undo?"
        ],
        "hello":[

            "😂 Hello aano... Hero aano bro?",

            "🤣 Hello parayan 2 manikkur edutho?",

            "😎 Hello accepted. Roast loading..."
        ]
        

    }
    
    reply = None

    if message : 

        found = False


        for keyword in roasts:

            if keyword in message.lower():

                replies = roasts[keyword]

                found = True

                break

        if not found:
            replies= [
                "😂 Bro... Athu enikku manassilaayilla.",

                "🤣 Kurachu simple ayi para bro.",

                "😎 BroRoast AI ippo training-il aanu."
            ]


        prompt = f"""
                    You are BroRoast AI.
        
                    Rules:
        
                    - Reply only in Malayalam (Manglish).
                    - Be funny.
                    - Roast the user in a friendly way.
                    - Never be rude.
                    - Maximum 2 sentences.
                    - Use emojis.
        
                    User Message:
                    {message}
                    """


        # reply = random.choice(replies)
        response = client.models.generate_content(

            model = "gemini-3.5-flash",

            contents=prompt

            

            
        )
        
        reply = response.text
        
        Chat.objects.create(
            user_message=message,
            bot_reply=reply
        )
        print(reply)
        

    # print(message)

    messages = Chat.objects.all().order_by("-id")

    total_chats = Chat.objects.count()

    

    return render(request,"home.html", {
        "message": message,
        "reply": reply,
        "messages": messages,
        "total_chats": total_chats,
    })


def delete_chat(request, id):

    chat = Chat.objects.get(id = id)

    chat.delete()

    return redirect("/")


def open_chat(request, id):

    chat = Chat.objects.get(id = id)

    messages = Chat.objects.all().order_by("-id")

    total_chats = Chat.objects.count()

    return render(request, "home.html", {
        "chat" : chat,
        "messages" : messages,
        "total_chats" : total_chats,
    })

def clear_chat(request):

    Chat.objects.all().delete()

    return redirect("/")
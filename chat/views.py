from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

def home(request):

    messages = []

    message = request.POST.get("message")

    # Dictionary (Only for Learning)
    roasts = {

        "hi": [
            "😂 Finally ezhunnetto?",
            "🤣 Coffee kudicho?"
        ],

        "bmw": [
            "🚗 Aadya cycle odikku bro.",
            "😂 BMW undo? Key mathram undo?"
        ]

    }
    
    reply = None

    if message : 

        if "hi" in message.lower():
            replies = [
                "😂 Bro... First nee urakkathil ninnu ezhunnetto? Pinne hi okke parayam.",
                "🤣 Bro... Coffee kudichittu vaa.",
                "😎 Finally online vannallo.",
                ]
            reply = random.choice(replies)

            messages.append({
                "user": message,
                "bot": reply,
            })
        

    # print(message)

    return render(request,"home.html", {
        "message": message,
        "reply": reply,
        "messages": messages,
    })
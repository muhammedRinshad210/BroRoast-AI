from django.shortcuts import render

# Create your views here.

import random

def home(request):

    messages = []

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
        ]

    }
    
    reply = None

    if message : 

        if message.lower() in roasts:
            replies = roasts[message.lower()]
            

            

        else:

            replies = [

                "😂 Bro... Athu enikku manassilaayilla.",

                "🤣 Kurachu simple ayi para bro.",

                "😎 BroRoast AI ippo training-il aanu. Veendum try cheyy."

            ]

        reply = random.choice(replies)

        messages.append({

                "user": message,

                "bot": reply

            })
        

    # print(message)

    return render(request,"home.html", {
        "message": message,
        "reply": reply,
        "messages": messages,
    })
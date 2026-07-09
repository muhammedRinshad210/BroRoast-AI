from django.shortcuts import render

# Create your views here.

import random
from .models import Chat

def home(request):

    messages = Chat.objects.all().order_by("-id")

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


        reply = random.choice(replies)

        
        Chat.objects.create(
            user_message=message,
            bot_reply=reply
        )
        

    # print(message)

    return render(request,"home.html", {
        "message": message,
        "reply": reply,
        "messages": messages,
    })
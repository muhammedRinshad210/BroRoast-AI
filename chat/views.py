from django.shortcuts import render, redirect

# Create your views here.

from .models import Chat
from .services import generate_reply, BOT_NAME



MAX_CONTEXT = 5







def get_previous_conversation():
    
    previous_chats = Chat.objects.all().order_by("-id")[:MAX_CONTEXT] 
    
    conversation = ""

    for chat in reversed(previous_chats):
        conversation += f"""
    user : {chat.user_message}
    {BOT_NAME} : {chat.bot_reply}
    """
    return conversation


def home(request):


    message = request.POST.get("message")

    conversation = get_previous_conversation()

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



        reply = generate_reply(
            message, conversation
        )


        
        
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
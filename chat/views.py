from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    message = request.POST.get("message")

    reply = None

    if message : 

        if "hi" in message.lower():
            reply = "😂 Bro... First nee urakkathil ninnu ezhunnetto? Pinne hi okke parayam."

        elif "python" in message.lower():
            reply = "🐍 Python padikkunnundo? Nice... snake alla bro, salary varunna language aanu."

        elif "bmw" in message.lower():
            reply = "🚗 BMW aano? Aadya cycle odichu balance padikku bro 😂"

        else:
            reply = f"😂 Bro... '{message}' paranjal njan ippo ithrayee roast cheyyu."
        

    # print(message)

    return render(request,"home.html", {
        "message": message,
        "reply": reply
    })
from django.http import HttpResponse
from django.conf import settings
from links.models import Link
import requests


def index(request):
    id = "137199697"

    q = Link.objects.filter(sended=False)

    for link in q:
        link.sended = True
        link.save()

        bot_message = f"[{link.text}]({link.text})"
        send_text = (
            "https://api.telegram.org/bot"
            + settings.BOT_TOKEN
            + "/sendMessage?chat_id="
            + id
            + "&parse_mode=Markdown&text="
            + bot_message
        )
        response = requests.get(send_text)

    return HttpResponse(response.json())
    # return HttpResponse(response)

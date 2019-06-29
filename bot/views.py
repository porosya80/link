from django.http import HttpResponse
from django.conf import settings
import requests


def index(request):
    id = "137199697"
    bot_message = "[link](gmail.com)"
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

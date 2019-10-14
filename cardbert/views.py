from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser
from cardbert.models import Card
from cardbert.serializers import CardSerializer


def card_parse(request, creditcard_number):
    # Get, so that it can be cached. Ignoring the fact that credit cards
    # should never be cached, nor sent unencrypted
    if (not creditcard_number) or (not creditcard_number.isdigit()):
        return JsonResponse(status=400, data={'status':'false','message':f'Invalid card number: {creditcard_number}'})
    serializer = CardSerializer(Card(number=creditcard_number))
    return JsonResponse(serializer.data, status=200)


def card_random(request, network=None):
    card = Card.random_for_network(network=network)
    if not card:
        return JsonResponse(status=404, data={'status':'false','message':f'Network {network} is not recognized.'})

    serializer = CardSerializer(card)
    return JsonResponse({card.number: serializer.data}, status=200)

from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser
from cardbert.models import Card
from cardbert.serializers import CardSerializer


def card_parse(request, creditcard_number):
    # Get, so that it can be cached. Ignoring the fact that credit cards
    # should never be cached, nor sent unencrypted
    serializer = CardSerializer(Card(number=creditcard_number))
    return JsonResponse(serializer.data, status=200)


def card_random(request, network=None):
    number = Card.random_for_network(network=network).number
    return JsonResponse({number: number}, status=200)

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from cardbert.models import Card
# from cardbert.serializers import CardSerializer

# class CardAPIView(APIView):
#     def post(self, request):
#         serializer = CardSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(pan=request.pan, status=Card.SENT)
#         return Response(status=status.HTTP_201_CREATED)


from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardbert.models import Card
from cardbert.serializers import CardSerializer

def card_parse(request, creditcard_number):
    # Get, so that it can be cached. Ignoring the fact that credit cards should never be cached, nor sent unencrypted

    # tmp = Card(mii='4', iin='411111')

    tmp = Card(number=creditcard_number)

    serializer = CardSerializer(Card(number=creditcard_number))

    import pdb; pdb.set_trace()
    return JsonResponse(serializer.data, status=200)

def card_random(request, network):
    raise NotImplementedError()
    
    
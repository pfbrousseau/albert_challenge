from rest_framework import serializers
from cardbert.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('mii', 'iin', 'pan', 'checkdigit', 'valid', 'network')

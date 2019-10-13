from cardbert.models import Card
from cardbert.constants import MC, V
from django.test import TestCase

class TestCard(TestCase):
    # Consider using Django's factory equivalent and adding a Card 
    def test_has_iin(self):
        card = Card(number='4'+'1'*15)
        assert(len(card.iin) == 6)
        assert(card.iin == '411111')
        
    def test_has_mii(self):
        card = Card(number='4'+'1'*15)
        assert(card.mii == '4')

    def test_has_description(self):
        card = Card(number='4'+'1'*15) 
        assert(card.mii_description == 'Banking and financial')

    def test_has_pan(self):
        card = Card(number='4'+'1'*15)
        assert(card.pan == '1'*10)


class TestNetworks(TestCase):
    def test_lower_mc(self):
        lowest_mc = '222100'
        assert len(MC) > 1  # Make sure Mastercard is defined
        assert Card(number=lowest_mc).network == MC
        
    def test_lowerbound(self):
        assert Card(number='222099').network is None

    def test_visa(self):
        assert len(V) > 1  # Make sure Visa is defined
        assert Card(number='400000000').network == V

    def test_visa_411(self):
        assert len(V) > 1  # Make sure Visa is defined

        # import pdb; pdb.set_trace()
        assert Card(number='4'+'1'*15).network == V, "Standard Visa test number should be recognized as Visa"
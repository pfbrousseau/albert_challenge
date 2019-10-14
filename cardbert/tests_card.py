from cardbert.models import Card
from cardbert.constants import MC, V
from django.test import TestCase


class TestCard(TestCase):
    # Consider using Django's factory equivalent and adding a Card
    def test_has_iin(self):
        card = Card(number='4' + '1' * 15)
        assert(len(card.iin) == 6)
        assert(card.iin == '411111')

    def test_has_mii(self):
        card = Card(number='4' + '1' * 15)
        assert(card.mii == '4')

    def test_has_description(self):
        card = Card(number='4' + '1' * 15)
        assert(card.mii_description == 'Banking and financial')

    def test_has_pan(self):
        card = Card(number='4' + '1' * 15)
        assert(card.pan == '1' * 10)

    def test_valid(self):
        card = Card(number='4' + '1' * 15)
        assert(card.valid)

    def test_invalid(self):
        card = Card(number='4' + '1' * 14 + '0')
        assert(not card.valid)


class TestNetworks(TestCase):
    def test_lower_mc(self):
        lowest_mc = '222100'
        assert len(MC) > 1  # Make sure Mastercard is defined
        assert Card(number=lowest_mc).network == MC

    def test_lowerbound(self):
        assert Card(number='222099').network is None

    def test_upperbound(self):
        assert Card(number='999999').network is None

    def test_visa(self):
        assert len(V) > 1  # Make sure Visa is defined
        assert Card(number='400000000').network == V

    def test_visa_411(self):
        assert Card(
            number='4' + '1' * 15).network == V, "Standard Visa test number should be recognized as Visa"

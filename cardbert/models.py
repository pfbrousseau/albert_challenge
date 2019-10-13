from bisect import bisect_right

from cardbert.constants import NETWORK_RANGES, NETWORK_RANGES_KEYS, MII_CHOICES_DICT, IIN_LENGTH
from django.db import models

from luhn import verify


class Card(models.Model):
    # created = models.DateTimeField(auto_now_add=True)

    # Using chars instead of Int when leading zeroes must be tracked, especially when length is not known

    number = models.CharField(max_length=19)

    # # https://en.wikipedia.org/wiki/ISO/IEC_7812#Major_industry_identifier
    # mii = models.CharField(
    #     choices=MII_CHOICES,
    #     max_length=1)  # Int or extract from iin

    # # https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
    # iin = models.CharField(max_length=8)
    # pan = models.CharField(max_length=12)
    # checkdigit = models.CharField(max_length=1)  # Could use Int

    # class Meta:
    #     ordering = ['iin', 'pan']

    # def pcisafe_number:
    #  first6_last4

    @property
    def mii(self):
        if not self.number:
            return None
        return self.number[0]

    @property
    def mii_description(self):
        return MII_CHOICES_DICT.get(str(self.mii))
    
    @property
    def iin(self):
        if not self.number:
            return None
        return self.number[:IIN_LENGTH]

    @property
    def pan(self):
        if not self.number:
            return None
        return self.number[IIN_LENGTH:]

    @property
    def checkdigit(self):
        if not self.valid: # If number is not valid, checkdigit doesn't make sense
            return None
        return self.number[-1]   

    @property
    def valid(self):
        return verify(self.number)

    @property
    def network(self):
        if len(self.iin) < 6:
            # debug: invalid IIN
            return None
        
        # Find the lowest number that comes before (or including) IIN
        left_key_index = bisect_right(NETWORK_RANGES_KEYS, int(self.iin)) - 1
        left_key = NETWORK_RANGES_KEYS[left_key_index]
        return NETWORK_RANGES[left_key]

    @classmethod
    def random_for_network(cls, network, length=16):
        """ Generate a Card object with a random number.

        Args:
            network (str):
            length (int, optional)

        Returns:
            Card: 
        """
        network_iin = network
        return cls(number='123456')

    # @classmethod
    # def from_number(cls, cc_number ):
    #     card = cls(iin=cc_number[:6])
    #     # do something with the book
    #     return card
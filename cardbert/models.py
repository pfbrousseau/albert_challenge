from bisect import bisect_right
import random

from cardbert.constants import NETWORK_RANGES, NETWORK_RANGES_KEYS, MII_CHOICES_DICT, IIN_LENGTH, NUMBER_FOR_NETWORK
from django.db import models

import luhn


class Card(models.Model):
    """
    Only attribute is the number as the others can be generated as needed.
    All other attributes are accessed through properties.
    Using chars instead of Int when leading zeroes must be tracked, especially when number length is not known
    """

    number = models.CharField(max_length=19)

    # https://en.wikipedia.org/wiki/ISO/IEC_7812#Major_industry_identifier
    @property
    def mii(self):
        if not self.number:
            return None
        return self.number[0]

    @property
    def mii_description(self):
        return MII_CHOICES_DICT.get(str(self.mii))

    # https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
    @property
    def iin(self):
        if not self.number:
            return None
        return self.number[:IIN_LENGTH]

    @property
    def pan(self):
        if not self.number:
            return None
        # Everything except IIN and checksum
        return self.number[IIN_LENGTH:-1]

    @property
    def checkdigit(self):
        if not self.valid:  # If number is not valid, checkdigit doesn't make sense
            return None
        return self.number[-1]

    # Consider making a cached property with `@functools.lru_cache()``
    @property
    def valid(self):
        if (not self.number) or (not self.number.isdigit()):
            return False
        return luhn.verify(self.number)

    @property
    def network(self):
        """
        Credit card network's name
            based on https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)

        Returns:
            Network (str) | None when no match is found or IIN is invalid.
        """
        if len(self.iin) < 6:
            # debug: Invalid IIN cannot have a network
            return None

        # Find the lowest number that comes before (or including) IIN
        left_key_index = bisect_right(NETWORK_RANGES_KEYS, int(self.iin)) - 1
        left_key = NETWORK_RANGES_KEYS[left_key_index]
        return NETWORK_RANGES[left_key]

    @classmethod
    def random_for_network(cls, network, length=16):
        """ Generate a Card object with a random number.

        Args:
            network (str): ['amercian_express'|discover_card'|'jcb'|'mastercard'|'visa']
            length (int, optional)

        Returns:
            card (Card): A valid card for network requested
                If no network is given, a random one will be chosen. 
                If network is given but not found, 'None' will be returned. Consider raising and catching instead
        """
        network_iin = cls.iin_from_network(network)
        if not network_iin:
            return None
        digit_count_remaining = length - len(network_iin) - 1  # -1 for checksum
        random_digits = ''.join(str(random.randint(0, 9))
                                for _ in range(digit_count_remaining))
        number = luhn.append(network_iin + random_digits)

        return cls(number=number)

    @classmethod
    def iin_from_network(cls, network=None):
        """
        Get the first matching IIN value for network. 
        This could be improved to give any random number in possible range but will work for now
        

        Args:
            network (str): ['amercian_express'|discover_card'|'jcb'|'mastercard'|'visa'|None] 

        Returns:
            iin (str): A iin for network (currently last defined starting range).
                If no network is given, a random one will be chosen. 
                If network is given but not found, 'None' will be returned
        """

        if network is None:
            return random.choice(list(NUMBER_FOR_NETWORK.values()))

        # Todo: Could get all matches as well as ending value (next index)
        iin = NUMBER_FOR_NETWORK.get(network.lower().replace(' ', '_'))
        # if iin is None:
        #     raise NetworkUnknownError

        return str(iin)


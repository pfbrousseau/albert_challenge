from django.db import models


# MII
# https://en.wikipedia.org/wiki/ISO/IEC_7812#Major_industry_identifier
MII_CHOICES = {'0': "ISO/TC 68 and other industry assignments",
'1': 'Airlines',
'2': 'Airlines, financial and other future industry assignments',
'3': 'Travel and entertainment',
'4': 'Banking and financial',
'5': 'Banking and financial',
'6': 'Merchandising and banking/financial',
'7': 'Petroleum and other future industry assignments',
'8': 'Healthcare, telecommunications and other future industry assignments',
'9': 'For assignment by national standards bodies'
}

class Card(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    # Using chars instead of in when leading zeroes must be tracked

    # https://en.wikipedia.org/wiki/ISO/IEC_7812#Major_industry_identifier
    mii = models.CharField(choices=MII_CHOICES, max_length=1)  # Int or extract from iin

    # https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)
    iin = models.CharField(max_length=8)
    pan = models.CharField(max_length=12)
    checkdigit = models.CharField(max_length=1)  # Could use Int
    
    class Meta:
        ordering = ['iin', 'pan']

    #def pcisafe_number:
    #  first6_last4
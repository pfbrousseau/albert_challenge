# Networks
# https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)

AE = 'American Express'
DC = 'Discover Card'
JCB = 'JCB'
MC = 'Mastercard'
V = 'Visa'

# Use None if end of range is not recognized. Network name if it is.
# To be used by `bisect`. Upper and lowerbounds should be None
NETWORK_RANGES = {
    222099: None,  # Lowerbound
    222100: MC, 272100: None,  # 2221-2720
    340000: AE, 350000: None,  # 34
    352800: JCB, 359000: None,  # 3528–3589
    370000: AE, 380000: None,  # 37
    400000: V, 500000: None,  # 4
    510000: MC, 560000: None,  # 51-55
    601100: DC, 601200: None,  # 6011
    622126: DC, 622926: None,  # 622126 - 622925
    624000: DC, 627000: None,  # 624000 - 626999
    628200: DC, 628900: None,  # 628200 - 628899
    640000: DC, 660000: None,  # 64, 65
}

# Perform this only once and store in a variable
NETWORK_RANGES_KEYS = sorted(NETWORK_RANGES.keys())

NUMBER_FOR_NETWORK = {name.lower().replace(' ', '_'): str(number) for (number, name) in NETWORK_RANGES.items() if name }


# MII
# https://en.wikipedia.org/wiki/ISO/IEC_7812#Major_industry_identifier
MII_CHOICES = (
    ('0', "ISO/TC 68 and other industry assignments"),
    ('1', 'Airlines'),
    ('2', 'Airlines, financial and other future industry assignments'),
    ('3', 'Travel and entertainment'),
    ('4', 'Banking and financial'),
    ('5', 'Banking and financial'),
    ('6', 'Merchandising and banking/financial'),
    ('7', 'Petroleum and other future industry assignments'),
    ('8', 'Healthcare, telecommunications and other future industry assignments'),
    ('9', 'For assignment by national standards bodies')
)
MII_CHOICES_DICT = dict(MII_CHOICES)

IIN_LENGTH = 6

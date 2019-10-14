# Albert Code Challenge #1: Credit Card Parser

## Installation (Python 3)

`pip install -r requirements.txt`

## Usage

### Running

`python manage.py runserver`

For production, make sure to disable settings.DEBUG, set settings.ALLOWED_HOSTS, hide the secret key, etc.

### Parse credit card number
GET `/card/{credit_card_number}`
Example Request: `curl 127.0.0.1:8000/card/4111111111111111`
Response: `{"mii": "4", "iin": "411111", "pan": "1111111111", "checkdigit": "1", "valid": true, "network": "Visa"}`

"network" will be null if no match is found
"checkdigit" will be null if card number is invalid (fails Luhn)

### Generate random credit card
GET `/card/random/{network}`
Args: network must be one of: ['amercian_express'|discover_card'|'jcb'|'mastercard'|'visa']
Example Request: `curl 127.0.0.1:8000/card/random/american_express`
Response: `{"3700003550876594": {"mii": "3", "iin": "370000", "pan": "355087659", "checkdigit": "4", "valid": true, "network": "American Express"}}`


## Test

python ./manage.py test

## Design Choices

* The main endpoint is a GET in order to allow for simple caching.
* Represent credit card number as a string to avoid problems with leading zeroes. 
* Only attribute to Card class is the number as the others can be generated as needed.
* Ignoring security concerns (unencrypted credit card being transmitted, cached). This should not be used when PCI-compliance is a concern. All of this code should run directly on the frontend prior to sending credit card number.
* Chose to use [PyPI's Luhn](https://pypi.org/project/luhn/) package due to its simplicity, speed, and maintainability. The code could easily be copied (only need a few lines) into this project, but I wanted to make it clear this code is not mine.
* Card Network indentification is done using python's bisect instead of regular expressions to greatly speed up the lookup. 
  - Bisect gives O(log(n)) instead of O(n)*O(regex), where n is the amount of networks. 
  - This could be further improved by using an optimized Trie (node '4' would give Visa, '3->7' would give Amercian Express)
  - Use 'None' to indicate the end of a defined range




## Requirements

Create an API that can validate credit cards and debit cards based solely on the card number. Given a card number, the api should return:
• Whether or not the card is valid
• The Major Industry Identifier (MII)
• The Issuer Identification Number (IIN)
• The personal account number
• The check digit

The API should be RESTful and use the various HTTP methods appropriately
• The API should be written in Python using Django for the web app backend
• Use the Luhn Algorithm to validate the card number
• Detect (at least) the 4 major US networks: Visa, MasterCard, Amex, and Discover

## ToDo
* Catch all 500s
* Finish bonus "random number for network"
* More documentation
* Code cleanup
* Add integration tests which call endpoints


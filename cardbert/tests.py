from django.test import TestCase
from rest_framework.test import APIRequestFactory


class TestCardAPI(TestCase):
    # Consider using Django's factory equivalent and adding a Card
    def test_happy_path_with_visa(self):
        url = '/card/4111111111111111'
        response = self.client.get(url)

        # Todo, break into subtests and check individual elements instead of exact string to improve 
        assert response.content == b'{"mii": "4", "iin": "411111", "pan": "111111111", "checkdigit": "1", "valid": true, "network": "Visa"}'

    def test_random_visa(self):
        url = '/card/random/visa'
        response = self.client.get(url)
        assert "Visa" in str(response.content)

    def test_random_american_express(self):
        url = '/card/random/american_express'
        response = self.client.get(url)
        body = str(response.content)
        assert "American Express" in body
        assert body.startswith('b\'{"34') or body.startswith('b\'{"37')

    def test_random_no_network(self):
        url = '/card/random/'
        response = self.client.get(url)
        assert '"valid": true' in str(response.content)

    def test_invalid_visa(self):
        url = '/card/4111111111111110'
        response = self.client.get(url)
        assert response.content == b'{"mii": "4", "iin": "411111", "pan": "111111111", "checkdigit": null, "valid": false, "network": "Visa"}'    

    def test_too_short(self):
        url = '/card/4111'
        response = self.client.get(url)
        assert '"network": null' in str(response.content)
    
    def test_letters(self):
        url = '/card/42a'
        response = self.client.get(url)
        assert response.status_code == 400
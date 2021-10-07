from django.test import TestCase
from ..models import Player

class PlayerTestCase(TestCase):

    def setUp(self):
        Player.objects.create(name='Juan', description='Friend', phone='0953662241')
        Player.objects.create(name='Alexander', description='Brother', phone='0999999999')

    def test_player_have_phone(self):
        soccer_player = Player.objects.get(name="Juan")
        basketbat_player = Player.objects.get(name="Alexander")
        self.assertEqual(soccer_player.phone(), "0953662241")
        self.assertEqual(basketbat_player.phone(), "0999999999")

import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticService(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()
        self.service = StatisticsService(self.reader)

    def test_search(self):
        player = self.service.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

    def test_search_no_player(self):
        player = self.service.search("Doe")
        self.assertEqual(player, None)

    def test_team(self):
        players = self.service.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top(self):
        players = self.service.top(3)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")

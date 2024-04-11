from unittest import TestCase, main

from project.tennis_player import TennisPlayer

if __name__ == '__main__':
    main()


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer('Ivan', 18, 10.0)

    def test_init(self):
        self.assertEqual(self.tennis_player.name, 'Ivan')
        self.assertEqual(self.tennis_player.age, 18)
        self.assertEqual(self.tennis_player.points, 10.0)
        self.assertEqual(self.tennis_player.wins, [])

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'Iv'
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_valid(self):
        self.tennis_player.add_new_win('Ivancho')
        self.assertEqual(self.tennis_player.wins, ['Ivancho'])
        self.tennis_player.add_new_win('Dragancho')
        self.assertEqual(self.tennis_player.wins, ['Ivancho', 'Dragancho'])

    def test_add_new_win_invalid(self):
        self.tennis_player.add_new_win('Ivancho')
        self.assertEqual(self.tennis_player.wins, ['Ivancho'])
        result = self.tennis_player.add_new_win('Ivancho')
        self.assertEqual(result, "Ivancho has been already added to the list of wins!")
        self.assertEqual(self.tennis_player.wins, ['Ivancho'])

    def test_lt_self_wins(self):
        other = TennisPlayer('Draganchou', 18, 9.0)
        self.assertEqual(self.tennis_player.points < other.points, False)
        self.assertEqual(self.tennis_player < other, 'Ivan is a better player than Draganchou')

    def test_lt_other_wins(self):
        other = TennisPlayer('Draganchou', 18, 11.0)
        self.assertEqual(self.tennis_player.points < other.points, True)
        self.assertEqual(self.tennis_player < other, 'Draganchou is a top seeded player and he/she is better than Ivan')

    def test_str(self):
        self.tennis_player.add_new_win('Ivancho')
        self.tennis_player.add_new_win('Dragancho')
        result = str(self.tennis_player)
        expected = f"Tennis Player: Ivan\nAge: 18\nPoints: 10.0\nTournaments won: Ivancho, Dragancho"
        self.assertEqual(result, expected)

from unittest import TestCase, main

from project.movie import Movie

if __name__ == '__main__':
    main()


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie('Movie', 2000, 9.8)

    def test_init(self):
        self.assertEqual(self.movie.name, 'Movie')
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 9.8)
        self.assertEqual(self.movie.actors, [])

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor_when_request_is_valid(self):
        self.assertEqual(self.movie.actors, [])
        self.movie.add_actor('Actor')
        self.assertEqual(self.movie.actors, ['Actor'])

    def test_add_actor_when_request_is_invalid(self):
        self.assertEqual(self.movie.actors, [])
        self.movie.add_actor('Actor')
        self.movie.add_actor('Actor')
        self.assertEqual(self.movie.actors, ['Actor'])
        self.assertEqual(self.movie.add_actor('Actor'), f"Actor is already added in the list of actors!")

    def test_greater_than_if_self_is_greater_than_other(self):
        other = Movie('Other movie', 2001, 7)
        self.assertEqual(self.movie.__gt__(other), f'"Movie" is better than "Other movie"')

    def test_greater_than_if_other_is_greater_than_self(self):
        other = Movie('Other movie', 2001, 10)
        self.assertEqual(self.movie.__gt__(other), f'"Other movie" is better than "Movie"')

    def test_repr(self):
        self.movie.add_actor('Actor')
        expected = f"Name: Movie\n" \
               f"Year of Release: 2000\n" \
               f"Rating: 9.80\n" \
               f"Cast: Actor"

        self.assertEqual(expected, str(self.movie))

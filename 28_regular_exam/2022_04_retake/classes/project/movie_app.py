from typing import List, Optional

from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def get_registered_users(self, username: str) -> Optional[User]:
        user = next(filter(lambda u: u.username == username, self.users_collection), None)
        return user

    def get_movie(self, title: str) -> Optional[Movie]:
        existing_movie = [m for m in self.movies_collection if m.title == title]
        if existing_movie:
            return existing_movie[0]
        return None

    def register_user(self, username: str, age: int):
        existing_user = self.get_registered_users(username)
        if existing_user:
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        existing_user = self.get_registered_users(username)

        if not existing_user:
            raise Exception("This user does not exist!")

        if movie.owner.username != existing_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        existing_movie = self.get_movie(movie.title)

        if existing_movie:
            raise Exception("Movie already added to the collection!")
        self.movies_collection.append(movie)
        existing_user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        existing_user = self.get_registered_users(username)

        existing_movie = self.get_movie(movie.title)

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if existing_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        existing_movie = self.get_movie(movie.title)

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        existing_user = self.get_registered_users(username)

        if movie.owner.username != existing_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        existing_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        existing_movie = self.get_movie(movie.title)
        existing_user = self.get_registered_users(username)

        if movie.owner.username == existing_user.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        already_liked = [m for m in existing_user.movies_liked if m.title == movie.title]
        if already_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        existing_user.movies_liked.append(movie)
        existing_movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        existing_movie = self.get_movie(movie.title)
        existing_user = self.get_registered_users(username)

        already_liked = [m for m in existing_user.movies_liked if m.title == movie.title]
        if not already_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        existing_user.movies_liked.remove(movie)
        existing_movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        if sorted_movies:
            return "\n".join([m.details() for m in sorted_movies])
        return "No movies found."

    def __str__(self):

        if self.users_collection:
            result = f"All users: {', '.join([u.username for u in self.users_collection])}\n"
        else:
            result = "All users: No users.\n"

        if self.movies_collection:
            result += f"All movies: {', '.join([m.title for m in self.movies_collection])}"
        else:
            result += "All movies: No movies."

        return result



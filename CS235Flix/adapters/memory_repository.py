from CS235Flix.adapters.repository import *
from CS235Flix.datafilereaders.movie_file_csv_reader import *
from CS235Flix.domain.model import *

class MemoryRepository(AbstractRepository):
    def __init__(self, filename):
        csvfile = MovieFileCSVReader(filename)
        csvfile.read_csv_file()
        self.repository_actors = csvfile.dataset_of_actors
        self.repository_directors = csvfile.dataset_of_directors
        self.repository_genres = csvfile.dataset_of_genres
        self.repository_movies = csvfile.dataset_of_movies
        self.repository_users = [User('login', 'password')]

    def add_user(self, user: User):
        self.repository_users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self.repository_users if user.user_name == username), None)

    def add_movie(self, movie: Movie):
        self.repository_movies.append(movie)

    def get_movie(self, movie_title) -> Movie:
        return next((movie for movie in self.repository_movies if movie.title == movie_title), None)

    def add_actor(self, actor: Actor):
        self.repository_actors.append(actor)

    def get_actor(self, actor_name) -> Actor:
        return next((actor for actor in self.repository_actors if actor.actor_full_name == actor_name), None)

    def add_genre(self, genre: Genre):
        self.repository_genres.append(genre)

    def get_genre(self, genre_name) -> Genre:
        return next((genre for genre in self.repository_genres if genre.genre_name == genre_name), None)

    def add_director(self, director: Director):
        self.repository_directors.append(director)

    def get_director(self, director_name) -> Director:
        return next((director for director in self.repository_directors if director.director_full_name == director_name), None)

    def get_movie_by_id(self, id_num) -> int:
        return next((movie for movie in self.repository_movies if movie.id == id_num), None)

    def get_movie_runtime_minutes(self, runtime_minutes) -> int:
        return next((movie for movie in self.repository_movies if movie.runtime_minutes == runtime_minutes), None)
import abc

from CS235Flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from CS235Flix.domain.model import *

repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user: username) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie: movie_title) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor: actor_name) -> Actor:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self, genre: genre_name) -> Genre:
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director: director_name) -> Director:
        raise NotImplementedError


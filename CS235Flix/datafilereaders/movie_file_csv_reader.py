import csv
from CS235Flix.domain.model import *


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__user_file_name = 'Users.csv'
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []
        self.__dataset_of_users = []

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    @property
    def dataset_of_users(self):
        return self.__dataset_of_users

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            for row in movie_file_reader:

                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                self.__dataset_of_movies.append(movie)

                actors = row['Actors'].split(",")
                for actor_full_name in actors:
                    actor = Actor(actor_full_name)

                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor)
                    movie.actors.append(actor)

                director = Director(row['Director'])
                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(director)
                movie.director = director

                genres = row['Genre'].split(",")
                for genre in genres:
                    genre_type = Genre(genre)
                    if genre_type not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre_type)
                    movie.genres.append(genre)

                movie.id = int(row['Rank'])
                movie.runtime_minutes = int(row['Runtime (Minutes)'])
                movie.description = str(row['Description'])

        for actor in self.__dataset_of_actors:
            for movie in self.__dataset_of_movies:
                if actor in movie.actors:
                    actor.movies.append(movie)

        for genre in self.__dataset_of_genres:
            for movie in self.__dataset_of_movies:
                for genre in f"{movie.genres}":
                    pass

        for director in self.__dataset_of_directors:
            for movie in self.__dataset_of_movies:
                if director == movie.director:
                    director.movies.append(movie)

    def read_user_csv_file(self):
        with open(self.__user_file_name, mode='r', encoding='utf-8-sig') as csvfile:
            user_file_reader = csv.DictReader(csvfile)
            for row in user_file_reader:
                username = row['username']
                password = row['password']
                user = User(username, password)
                self.__dataset_of_users.append(user)
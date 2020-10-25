from datetime import datetime


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__actor_colleagues_set = []
        self.__movies = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __str__(self):
        return f"{self.__actor_full_name}"

    def __eq__(self, other):
        return self.__actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__actor_colleagues_set.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__actor_colleagues_set:
            return True
        else:
            return False

    @property
    def movies(self):
        return self.__movies

    @movies.setter
    def movies(self, movie):
        if type(movie) == list:
            self.__movies = movie

    def add_movie(self, movie):
        self.__movies.append(movie)

    def remove_movie(self, movie):
        if movie in self.__movies:
            index = self.__movies.index(movie)
            self.__movies.pop(index)

    def get_movie_list(self):
        return ", ".join([str(movie) for movie in self.movies])

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()
        self.__movies = []


    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __str__(self):
        return f"{self.__director_full_name}"

    def __eq__(self, other):
        return self.__director_full_name == other.director_full_name

    def __lt__(self, other):
        return self.__director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)

    @property
    def movies(self):
        return self.__movies

    @movies.setter
    def movies(self, movie):
        if type(movie) == list:
            self.__movies = movie

    def add_movie(self, movie):
        self.__movies.append(movie)

    def remove_movie(self, movie):
        if movie in self.__movies:
            index = self.__movies.index(movie)
            self.__movies.pop(index)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()
        self.__movies = []

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __str__(self):
        return f"{self.__genre_name}"

    def __eq__(self, other):
        return self.__genre_name == other.genre_name

    def __lt__(self, other):
        return self.__genre_name < other.genre_name

    def __hash__(self):
        return hash(self.__genre_name)

    @property
    def movies(self):
        return self.__movies

    @movies.setter
    def movies(self, movie):
        if type(movie) == list:
            self.__movies = movie

    def add_movie(self, movie):
        self.__movies.append(movie)

    def remove_movie(self, movie):
        if movie in self.__movies:
            index = self.__movies.index(movie)
            self.__movies.pop(index)


class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year < 1900 or release_year == "" or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__description = ""
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__id = None

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        if id == "" or type(id) is not int:
            self.__id = None
        else:
            self.__id = id

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year: int):
        if release_year < 1900 or release_year == "" or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __str__(self):
        return f"{self.__title}, {self.__release_year}"

    def __eq__(self, other):
        self_title_and_release = self.__title + str(self.__release_year)
        other_title_and_release = other.__title + str(other.__release_year)
        return self_title_and_release == other_title_and_release

    def __lt__(self, other):
        self_title_and_release = self.__title + str(self.__release_year)
        other_title_and_release = other.__title + str(other.__release_year)
        return self_title_and_release < other_title_and_release

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director: Director):
        if type(director) == Director:
            self.__director = director

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors):
        if type(actors) == list:
            self.__actors = actors

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        if type(genres) == list:
            self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is not int or runtime_minutes < 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime_minutes

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            index = self.__actors.index(actor)
            self.__actors.pop(index)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            index = self.__genres.index(genre)
            self.__genres.pop(index)

    def get_genre_list(self):
        return ", ".join([str(genre) for genre in self.genres])

    def get_actor_list(self):
        return ", ".join([str(actor) for actor in self.actors])


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self._movie: Movie = movie
        self._review_text: str = review_text
        if rating < 1 or rating > 10 or type(rating) is not int:
            self._rating = None
        else:
            self._rating: int = rating
        self._timestamp = datetime.today()

    def __repr__(self):
        return f"<Review: {self._review_text}>"

    def __eq__(self, other):
        if type(other) is not Review:
            return False
        else:
            return self._movie == other.movie and self._review_text == other.review_text and self._rating == other.rating and self._timestamp == other.timestamp


    @property
    def movie(self) -> Movie:
        return self._movie

    @property
    def review_text(self) -> str:
        return self._review_text

    @property
    def rating(self) -> int:
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp


class User:
    def __init__(self, user_name, password):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password.strip()
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.user_name

    def __lt__(self, other):
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes


class WatchList:
    def __init__(self):
        self.__watch_list = []

    def __repr__(self):
        return f"<WatchList {self.__watch_list}>"

    def __eq__(self, other):
        return self.__watch_list == other.watch_list

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watch_list):
            movie = self.__watch_list[self.n]
            self.n += 1
            return movie
        else:
            raise StopIteration

    def add_movie(self, movie: Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index < 0 or index >= len(self.__watch_list):
            return None
        else:
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) == 0:
            return None
        else:
            return self.__watch_list[0]
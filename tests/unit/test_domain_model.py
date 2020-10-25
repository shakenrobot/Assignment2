from CS235Flix.domain.model import *


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"

    def test_lol(self):
        director2 = Director("")
        assert director2.director_full_name is None

    def test_3(self):
        director3 = Director(42)
        assert director3.director_full_name is None


class TestGenreMethods:

    def test_genre_1(self):
        genre = Genre("Horror")
        assert repr(genre) == "<Genre Horror>"

    def test_genre_2(self):
        genre = Genre("")
        assert genre.genre_name is None

    def test_genre_3(self):
        genre = Genre(42)
        assert genre.genre_name is None


class TestActorMethods:

    def test_actor_1(self):
        actor = Actor("Angelina Jolie")
        assert repr(actor) == "<Actor Angelina Jolie>"

    def test_actor_2(self):
        actor = Actor("")
        assert actor.actor_full_name is None

    def test_actor_3(self):
        actor = Actor(42)
        assert actor.actor_full_name is None


class TestMovieMethods:

    def test_movie_1(self):
        movie = Movie("Moana", 2016)
        assert repr(movie) == "<Movie Moana, 2016>"


class TestReviewMethods:

    def test_review_1(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)
        assert repr(review) == "<Review: This movie was very enjoyable.>"


class TestWatchlistMethods:

    def test_watchlist_1(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        assert repr(watchlist) == '<WatchList [<Movie Moana, 2016>, <Movie Ice Age, 2002>, <Movie Guardians of the Galaxy, 2012>]>'

    def test_watchlist_2(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        assert watchlist.size() == 3

    def test_watchlist_3(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        watchlist.remove_movie(Movie("Moana", 2016))
        watchlist.remove_movie(Movie("Ice Age", 2002))
        assert repr(watchlist) == "<WatchList [<Movie Guardians of the Galaxy, 2012>]>"
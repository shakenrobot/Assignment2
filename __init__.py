from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

from CS235Flix import *
from CS235Flix.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


def create_app():
    app = Flask(__name__)
    app.secret_key = 'somesecretkey'

    filename = 'Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    movie_file_reader.read_user_csv_file()

    @app.route('/')
    def home():
        return render_template("index.html", content=movie_file_reader.dataset_of_movies)

    @app.route('/login/', methods=["GET", "POST"])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = [x for x in movie_file_reader.dataset_of_users if x.user_name == username][0]
            if user and user.password == password:
                session['user_name'] = username
                return redirect(url_for('home'))

            return redirect(url_for('home'))
        if request.method == 'GET':
            return render_template("loginPage.html")

    @app.route('/genres/')
    def genres():
        return render_template("GenresHTML.html", movies=movie_file_reader.dataset_of_movies, genres=movie_file_reader.dataset_of_genres)

    @app.route('/genres/<genre>/')
    def genre_hyperlink(genre):
        genre = str(genre)
        return render_template("Genresformat.html", genres=movie_file_reader.dataset_of_genres, movies=movie_file_reader.dataset_of_movies, genre=genre)

    @app.route('/actors/')
    def actors():
        return render_template("ActorsHTML.html", actors=movie_file_reader.dataset_of_actors, movies=movie_file_reader.dataset_of_movies)

    @app.route('/actors/<actor>/')
    def actor_hyperlink(actor):
        actor = str(actor)
        return render_template("Actorsformat.html", actors=movie_file_reader.dataset_of_actors, movies=movie_file_reader.dataset_of_movies, actor=actor)

    @app.route('/movies/')
    def movies():
        return render_template("MoviesHTML.html", movies=movie_file_reader.dataset_of_movies)

    @app.route('/movies/<movie>/')
    def movie_hyperlink(movie):
        movie = int(movie)
        return render_template("Moviesformat.html", movies=movie_file_reader.dataset_of_movies, movie=movie)

    @app.route('/directors/')
    def directors():
        return render_template("DirectorsHTML.html", directors=movie_file_reader.dataset_of_directors, movies=movie_file_reader.dataset_of_movies)

    @app.route('/directors/<director>/')
    def director_hyperlink(director):
        director = str(director)
        return render_template("Directorsformat.html", directors=movie_file_reader.dataset_of_directors,
                               movies=movie_file_reader.dataset_of_movies, director=director)

    return app



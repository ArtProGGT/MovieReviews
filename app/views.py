from flask.templating import render_template
from flask.helpers import url_for, redirect
from .models import Movies, Reviews
from werkzeug.utils import secure_filename
from pathlib import Path
from . import application, database
from .forms import AddMovieForm, ReviewForm


BASE_DIR = Path(__file__).parent
UPLOAD_FOLDER = BASE_DIR / "static" / "images"


@application.route("/")
def index():
    movies = Movies.query.order_by(Movies.movie_id.desc()).all()

    return render_template("index.html", movies=movies)


@application.route("/movie/<int:movie_id>", methods=["GET", "POST"])
def movie(movie_id):
    movie = Movies.query.get(movie_id)
    form = ReviewForm(rating=10)
    if movie.reviews:
        avg_score = round(sum(review.rating for review in movie.reviews) / len(movie.reviews), 2)
    else:
        avg_score = 0
    if form.validate_on_submit():
        review = Reviews()
        review.author = form.author.data
        review.review_text = form.review_text.data
        review.rating = form.rating.data
        review.movie_id = movie.movie_id
        database.session.add(review)
        database.session.commit()

        return redirect(url_for("movie", movie_id=movie.movie_id))

    return render_template("movie.html", movie=movie, avg_score=avg_score, form=form)


@application.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movies()
        movie.name = form.name.data
        movie.description = form.description.data
        image = form.image.data
        image_name = secure_filename(image.filename)
        UPLOAD_FOLDER.mkdir(exist_ok=True)
        image.save(UPLOAD_FOLDER / image_name)
        movie.image = image_name
        database.session.add(movie)
        database.session.commit()

        return redirect(url_for("movie", movie_id=movie.movie_id))

    return render_template("add_movie.html", form=form)


@application.route("/reviews")
def reviews():
    reviews = Reviews.query.order_by(Reviews.created_at.desc()).all()

    return render_template("reviews.html", reviews=reviews)


@application.route("/delete_review/<int:review_id>")
def delete_review(review_id):
    review = Reviews.query.get(review_id)
    database.session.delete(review)
    database.session.commit()

    return redirect(url_for("reviews"))

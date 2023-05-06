from datetime import datetime
from flask_sqlalchemy.extension import SQLAlchemy
from . import database


# Таблица с фильмами
class Movies(database.Model):
    movie_id = database.Column(database.Integer, primary_key=True)                                              # ID фильма
    name = database.Column(database.String(255), nullable=False, unique=True)                                   # Название фильма
    description = database.Column(database.Text, nullable=False)                                                # Описание фильма
    image = database.Column(database.String(255), nullable=False)                                               # Постер фильма
    reviews = database.relationship("Reviews", back_populates="movie")                                          # Связь с отзывами из таблицы Reviews


# Таблица с отзывами
class Reviews(database.Model):
    review_id = database.Column(database.Integer, primary_key=True)                                             # ID отзыва
    author = database.Column(database.String(255), nullable=False)                                              # Имя автора отзыва
    review_text = database.Column(database.String(255), nullable=False)                                         # Текст отзыва
    created_at = database.Column(database.DateTime, default=datetime.utcnow)                                    # Дата создания отзыва
    rating = database.Column(database.Integer, nullable=False)                                                  # Оценка автора
    movie_id = database.Column(database.Integer, database.ForeignKey("movies.movie_id", ondelete="CASCADE"))     # ID фильма из таблицы фильмов
    movie = database.relationship("Movies", back_populates="reviews")                                           # Связь с фильмами из таблицы Movie

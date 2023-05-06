from wtforms.fields.simple import StringField, TextAreaField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired
from flask_wtf.form import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired


class ReviewForm(FlaskForm):
    author = StringField("Ваше имя", validators=[DataRequired(message="Поле не должно быть пустым")])
    review_text = TextAreaField("Текст отзыва", validators=[DataRequired(message="Поле не должно быть пустым")])
    rating = SelectField(choices=[(i, i) for i in range(1, 11)])
    submit = SubmitField("Добавить отзыв")


class AddMovieForm(FlaskForm):
    name = StringField("Название", validators=[DataRequired(message="Поле не должно быть пустым")])
    description = TextAreaField("Описание", validators=[DataRequired(message="Поле не должно быть пустым")])
    image = FileField("Изображение", validators=[FileRequired(message="Поле не должно быть пустым"), FileAllowed(["jpg", "jpeg", "png"], message="Неверный формат файла")])
    submit = SubmitField("Добавить фильм")

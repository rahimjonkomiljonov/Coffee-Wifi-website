from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', validators=[DataRequired()],choices=[
        ('1', '☕️'),
        ('2', '☕️☕️'),
        ('3', '☕️☕️☕️'),
        ('4', '☕️☕️☕️☕️'),
        ('5', '☕️☕️☕️☕️☕️')
    ])
    wifi = SelectField('WIFI rating', validators=[DataRequired()], choices=[
        ('1', '✘'),
        ('2', '💪'),
        ('3', '💪💪'),
        ('4', '💪💪💪'),
        ('5', '💪💪💪💪'),
        ('6', '💪💪💪💪💪')
    ])
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=[
        ('1', '✘'),
        ('2', '🔌'),
        ('3', '🔌🔌'),
        ('4', '🔌🔌🔌'),
        ('5', '🔌🔌🔌🔌'),
        ('6', '🔌🔌🔌🔌🔌')
    ])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
with open('static/css/styles.css', 'r') as css_file:
    css_content = css_file.read()

# all Flask routes below
@app.route("/")
def home():

    return render_template("index.html", css_content=css_content)


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form, css_content=css_content)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows, css_content=css_content)


if __name__ == '__main__':
    app.run(debug=True)

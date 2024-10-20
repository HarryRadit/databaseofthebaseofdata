from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "IMGAY"
db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    #dob = db.Column(db.String(100))
   #gender = db.Column(db.String(100))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.dob = dob
        #self.gender = gender

@app.route('/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
       #dob = request.form['dob']
        #gender = request.form['gender']


        student = Students(name, age,)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('show_details.html'))
    return render_template('add_student.html')

@app.route('/show_details.html')
def show_details():
    return render_template('show_details.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=8081)

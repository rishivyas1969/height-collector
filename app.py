from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import count
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:rishi1969@localhost:5432/height_collector'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://cccmxzxtntzroq:e4c92fc032b8d4b6d00e4385dc0791c42f49d78c5e406732defe435f4e06e7a6@ec2-44-194-6-121.compute-1.amazonaws.com:5432/dfk93uhn66s9c4?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id=db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=["POST"])
def success():

    if request.method=='POST':
        email = request.form['email_name']
        height = request.form['height_name']
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data=Data(email, int(height))
            db.session.add(data)
            db.session.commit()
            count_height = db.session.query(Data.height_).count()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 2)
            send_email(email, height, average_height, count_height)
            return render_template("success.html")
    return render_template("index.html", text="Seems like we already have your email!")

if __name__ == '__main__':
    app.debug=True
    app.run()

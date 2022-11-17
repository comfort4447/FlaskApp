from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy




# def create_app():
app = Flask(__name__)
    


with app.app_context():
    app = current_app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5433/postgres' 
    db = SQLAlchemy(app)



    class Person(db.Model):
        __tablename__ ='persons'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person #{self.id} {self.name}'

    db.create_all()

    @app.route('/')
    def index():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=3000)

   

    
from flask import Flask, current_app


import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

with app.app_context():
	# curr_app = current_app
	# curr_app.run(debug=True, use_reloader=False, host='0.0.0.0')
	app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://abisolatayo@localhost:5432/postgres'
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db = SQLAlchemy(app)
	migrate = Migrate(app, db)
	db.create_all()

	class Person(db.Model):
		__tablename__ = 'persons'
		id = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(), nullable=False)

	def __repr__(self):
		return f'<Person ID:{self.id} name: {self.name}'

	# db.create_all()
	db.session.commit()

	# import api
	# api.add_all_apis(app=app)

@app.route('/')
def index():
	person = Person.query.first()
	return 'Hello ' + person.name

if __name__ == "__main__":
	app.run(debug=False)
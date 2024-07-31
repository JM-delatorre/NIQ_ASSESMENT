from flask import jsonify
from models.greeting_model import Greeting
from config.db import db


def serialize_greeting(greeting):
    return {
        'id': greeting.id,
        'name': greeting.name,
        'timestamp': greeting.timestamp
    }

def get_greetings():
    try:
      greetings = Greeting.query.all()
      return jsonify([serialize_greeting(greeting) for greeting in greetings])
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

def create_greeting(data):
    if not data or 'name' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'The "name" field is required.'}), 400

    if not isinstance(data['name'], str) or not data['name'].strip():
        return jsonify({'error': 'Bad Request', 'message': 'The "name" field must be a non-empty string.'}), 400
    try:
      new_greeting = Greeting(name=data['name'])
      db.session.add(new_greeting)
      db.session.commit()
      return jsonify({'message': "Hello {}".format(new_greeting.name)}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

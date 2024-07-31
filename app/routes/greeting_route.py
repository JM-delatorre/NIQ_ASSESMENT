from flask import current_app as app
from flask import request
from controllers.greeting_control import create_greeting, get_greetings

@app.route('/hello', methods=['POST'])
def add_greeting():
    data = request.get_json()
    return create_greeting(data)

@app.route('/list', methods=['POST'])
def fetch_greetings():
    return get_greetings()

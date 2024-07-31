from flask import Flask
from config.env import Config
from config.db import db
import logging

app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)


with app.app_context():
    import routes.greeting_route 
    db.create_all()  

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=8080)

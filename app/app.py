from flask import Flask

from app.routes.calendar_routes import calendar_bp
from app.routes.tasks_routes import tasks_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(tasks_bp, url_prefix='/api')
    app.register_blueprint(calendar_bp, url_prefix='/api/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
from flask import Flask, request, abort, jsonify
from models import setup_db
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/": {"origins": "http://localhost:3000"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )

        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,DELETE"
        )

        response.headers.add(
            'Access-Control-Allow-Origin', 'http://localhost:3000'
        )

        response.headers.add(
            'Access-Control-Allow-Credentials', 'true'
        )

        return response

    @app.route("/")
    def main_route():
        return jsonify({"success": True, "message": "Configuration Successful"})

    return app

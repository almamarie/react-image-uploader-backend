from flask import Flask, request, abort, jsonify


def create_app(test_config=None):
    app = Flask(__name__)

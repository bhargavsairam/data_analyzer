from flask import Blueprint, jsonify, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/data')
def data():
    return jsonify({'message': 'Hello from Flask!'})
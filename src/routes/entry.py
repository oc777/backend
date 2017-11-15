from flask import Blueprint, jsonify
entry = Blueprint('entry', __name__)

@entry.route('/')
def getEntry():
  routes = {
    'admins': '/admins',
    'self': '/'
  }
  return jsonify(routes)

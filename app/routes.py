from flask import Blueprint, request, jsonify, abort
from .models import db, Messages, Likes

api = Blueprint("main", __name__)

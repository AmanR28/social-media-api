from flask import Blueprint, request, jsonify, abort
from .models import db, Messages, Likes

api = Blueprint("main", __name__)

# Handling Errors
class Error:
    MISSING_USER_ID="user_id not found"
    MISSING_MESSAGE_ID='message_id not found'
    MISSING_MESSAGE='message not found'
    DB_ERROR='Something went wrong'


# Route : Get Messages List
@api.route('/messages', methods=['GET'])
def get_messages():
    try:
        messages = Messages.query.order_by(Messages.timestamp.desc()).all()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify([message.to_dict() for message in messages]), 200


# Route : Post New Message
@api.route('/messages', methods=['POST'])
def post_message():
    user_id = request.form.get("user_id")
    message = request.form.get("message")
    if not user_id:
        abort(400, Error.MISSING_USER_ID)
    if not message:
        abort(400, Error.MISSING_MESSAGE)

    try:
        msg = Messages(user_id=user_id, message=message)
        db.session.add(msg)
        db.session.commit()
    except Exception:
        abort(500, Error.DB_ERROR)
    
    return jsonify('Message Posted'), 201
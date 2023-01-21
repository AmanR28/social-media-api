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


# Route : Get Like Count for Particular Message
@api.route('/messages/likes', methods=['GET'])
def get_likes():
    message_id = request.form.get("message_id")
    if not message_id:
        abort(400, Error.MISSING_MESSAGE_ID)

    try:
        msg = Messages.query.filter_by(id=message_id).first()
    except Exception:
        abort(500, Error.DB_ERROR)

    return jsonify({'likes': msg.likes}), 200


# Route : Like a Message
@api.route('/messages/likes', methods=['POST'])
def like_message():
    message_id = request.form.get("message_id")
    user_id = request.form.get("user_id")
    if not message_id:
        abort(400, Error.MISSING_MESSAGE_ID)
    if  not user_id:
        abort(400, Error.MISSING_USER_ID)
    
    try:
        like = Likes(
            message_id=message_id, user_id=user_id)
        db.session.add(like)
        db.session.commit()
    except Exception:
        abort(500, Error.DB_ERROR)
    
    return jsonify('Message Liked'), 201


# Route : Dislike a Message
@api.route('/messages/likes', methods=['DELETE'])
def delete_message():
    message_id = request.form.get("message_id")
    user_id = request.form.get("user_id")
    if not message_id:
        abort(400, Error.MISSING_MESSAGE_ID)
    if  not user_id:
        abort(400, Error.MISSING_USER_ID)
    
    try:
        like = Likes.query.filter_by(message_id=message_id, user_id=user_id).first()
        db.session.delete(like)
        db.session.commit()
    except Exception:
        abort(500, Error.DB_ERROR)
    
    return jsonify('Message Disliked'), 201
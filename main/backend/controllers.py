from flask import request, jsonify, abort
from .services import get_token_data, update_token_price
from .models import Session, User, Token

# Controller to get data for a specific token
def token_data_controller(symbol):
    data = get_token_data(symbol)
    if data:
        return jsonify(data), 200
    else:
        abort(404, description="Token data not found.")

# Controller to update the price of a token
def update_token_price_controller(token_id):
    price = request.json.get('price', None)
    if price:
        update_token_price(token_id, price)
        return jsonify({"message": "Token price updated successfully."}), 200
    else:
        abort(400, description="No price provided.")

# Controller to add a new token for a user (example with user authentication)
def add_token_to_user_controller(user_id):
    symbol = request.json.get('symbol', None)
    if not symbol:
        abort(400, description="No symbol provided.")

    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        new_token = Token(symbol=symbol, user_id=user.id)
        session.add(new_token)
        session.commit()
        session.close()
        return jsonify({"message": f"Token {symbol} added to user {user.username}."}), 201
    else:
        session.close()
        abort(404, description="User not found.")

# TODO: Define more controllers for other functionalities like user registration, authentication, etc.

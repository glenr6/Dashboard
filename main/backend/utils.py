import os
from functools import wraps
from flask import request, jsonify, abort

# Utility function for API key loading
def load_api_key(service_name):
    return os.getenv(f'{service_name}_API_KEY')

# Decorator for validating API keys in incoming requests
def require_api_key(api_key):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            key = request.headers.get('X-API-KEY')
            if key and key == api_key:
                return f(*args, **kwargs)
            else:
                abort(401, description="Invalid API Key")
        return decorated_function
    return decorator

# Error handling utility
def handle_error(status_code, message):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response

# TODO: Add more utility functions as needed for logging, data formatting, etc.

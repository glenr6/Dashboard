from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Dashboard Backend Running!"

# Placeholder for future API routes
# TODO: Add routes for user authentication
# TODO: Add routes for fetching and displaying cryptoasset data

if __name__ == '__main__':
    app.run(debug=True) # Set debug to False in production

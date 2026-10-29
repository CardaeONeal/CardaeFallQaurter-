# import the flask library into this file
from flask import Flask 

# Create a new Flask app named "app"
app = Flask(__name__)

#Create a home page for our Flask app (website)
@app.route('/') # The route for the home page
def Index():
    return "Hello,World"

if __name__ == '__main__':
    app.run(debug = True)

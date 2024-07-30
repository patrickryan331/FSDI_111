from flask import Flask                    # from the flask module import the Flask class instance

app  = Flask(__name__)

@app.get("/aboutme")                              # flask decorator that "wraps" our view function
def index():                               # view function
    me = {                                 # python3 dictionary (key-value pairs)
        "first_name": "Patrick",
        "last_name": "Ryan",
        "hobbies": "Surfing, Skiing, Video Games",
        "is_online": True
    }
    return me                              # returning a dictionary from a view function automatically converted to JSON!

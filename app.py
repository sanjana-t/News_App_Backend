from flask import Flask,request
from stories import send_stories,send_comments,send_newstories
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/getStories", methods=['GET'])
def stories():
    # request_data = request.json
    response = send_stories()
    return response

@app.route("/getComments", methods=['POST'])
def comments():
    request_data = request.json
    response = send_comments(request_data)
    return response

@app.route("/getnewStories", methods=['GET'])
def newstories():
    response = send_newstories()
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port='6001')
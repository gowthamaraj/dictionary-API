import json
from difflib import get_close_matches
from flask import Flask,jsonify

data = json.load(open("data.json"))
app = Flask(__name__)

@app.route('/dict/<string:word>', methods=['GET'])
def dict(word):
    result = find(word)
    return jsonify(result)

def find(word):
    try:
        return {"definiton":data[word]}
    except KeyError:
        if len(get_close_matches(word,data.keys(),cutoff =0.8))>0:
            return {"match":get_close_matches(word,data.keys(),cutoff =0.8)[0]}
        return {"error":"Word does not exist!"}

if __name__ == "__main__":
    app.run(debug=True)
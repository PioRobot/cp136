from flask import request,jsonify,Flask
from data import data

app=Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,"message":"succes"}),200

@app.route("/planet")
def index2():
    name =request.args.get("name")
    planet_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":planet_data,"message":"succes"}),200

if __name__=="__main__":
    app.run()
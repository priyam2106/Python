from flask import Flask,jsonify

app = Flask(__name__)



@app.route("/")
def json():
    marks ={
    "Harry": 56,
    "Rohan":67,
    "Akash":33,
    "Priyam":100,
    "Panoti":32
    }
    values =[1,marks,67]
    return jsonify(values)


app.run(debug=True)
1.
# # app.py
# from flask import Flask, jsonify

# import json

# app = Flask(__name__)

# @app.route("/api")
# def get_data():
#     with open("data.json", "r") as file:
#         data = json.load(file)
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(debug=True)


2. 
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient("mongodb+srv://jatinjoshi1045:jatin1045@cluster0.dagn2mi.mongodb.net/your_mongodb_atlas_connection_string")
db = client["form_data"]
collection = db["submissions"]

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        try:
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            flash(f"Error: {str(e)}")
            return render_template("form.html")
    return render_template("form.html")

@app.route("/success")
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)


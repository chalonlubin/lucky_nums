from flask import Flask, render_template, request, jsonify
from random import randint
from forms import ValidationForm
import requests


app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


NUMBERS_API_URL = "http://numbersapi.com/"



@app.get("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

# @app.post("/api/get-lucky-num")
# def get_lucky():
#     """API endpoint. Returns JSON. """

#     errors = {}
#     colors = ["red", "green", "orange", "blue"]

#     if request.json["name"] == "":
#         errors["name"] = "This field is required."
#     if request.json["email"] == "":
#         errors["email"] = "This field is required."
#     if request.json["year"] == "":
#         errors["year"] = "This field is required."
#     else:
#         if int(request.json["year"]) >= 2000 or int(request.json["year"]) <= 1900:
#             errors["year"] = "Must be born between 1900 and 2000 to play."
#     if request.json["color"] == "":
#         errors["color"] = "This field is required."
#     else:
#         if request.json["color"] not in colors:
#             errors["color"] = "Invalid value, must be one of: red, green, orange, blue."

#     if len(errors) > 0:
#         return jsonify({"error": errors})
#     else:
#         year = request.json["year"]
#         random_num = randint(1,100)

#         num_fact = requests.get(
#             f"http://numbersapi.com/{random_num}")
#         year_fact = requests.get(
#             f"http://numbersapi.com/{year}")

#         response = {
#             "num": {
#                 "fact": num_fact.text,
#                 "num": random_num
#             },
#             "year": {
#                 "fact": year_fact.text,
#                 "year": year
#             }
#         }

#         return jsonify(response)


@app.post("/api/get-lucky-num")
def get_lucky():
    """API endpoint. Returns JSON. """

    user_input = {
        "name": request.json["name"],
        "email": request.json["email"],
        "year": request.json["year"],
        "color": (request.json["color"]),
    }

    form = ValidationForm(obj=user_input)

    if form.validate():
        year = int(request.json["year"])
        random_num = randint(1, 100)

        num_fact = requests.get(
            f"http://numbersapi.com/{random_num}")
        year_fact = requests.get(
            f"http://numbersapi.com/{year}")

        response = {
            "num": {
                "fact": num_fact.text,
                "num": random_num
            },
            "year": {
                "fact": year_fact.text,
                "year": year
            }
        }
        return jsonify(response)

    return jsonify({"error": form.errors})

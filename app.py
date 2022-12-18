from flask import Flask, render_template, request, jsonify
from forms import LuckyNumForm
from utilities import random_number, serialize_random_facts

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


@app.get("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.post("/api/get-lucky-num")
def get_lucky():
    """API endpoint. Returns JSON response based off WTForms validation. """

    user_input = {
        "name": request.json["name"],
        "email": request.json["email"],
        "year": request.json["year"],
        "color": request.json["color"],
    }

    form = LuckyNumForm(obj=user_input)

    if form.validate():
        year = user_input["year"]
        num = random_number(1,100)
        response = serialize_random_facts(num, year)

        return jsonify(response)

    return jsonify({"error": form.errors})


############################ Non-Extra Credit Way:
# Just in case you needed to see it here is the original code.
# I would of moved my functions to another .py file
# for seperation of concerns, however this
# was just the raw code to get the app up and running.

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

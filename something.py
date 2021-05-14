# Importing the Pickle File
pkl_import = open('MNB_classifier.pkl', 'rb')
classifier = pickle.load(pkl_import)

# Initialising the  Flask and Swagger
app = Flask(__name__, template_folder="templates")
Swagger(app)


# Creating the Base Route
@app.route('/', methods=['GET'])
def welcome_message():
    try:
        return render_template("home.html"), 200
    except Exception as e:
        return "something went wrong", 400


# Creeating a route for Prediction
@app.route('/predict', methods=['GET'])
def predict():
    """Testing of Review prediction .
    ---
    parameters:
      - name: review
        in: query
        type: string
        required: true
    responses:
        200:
            description: The response is

    """

    review = request.args.get("review")

    result = classifier.predict([review])
    return f"The result are as follows {result}"
    # if result in [0,"0"] :  return "Fake Bank Note",200
    # return "Valid bank note",200


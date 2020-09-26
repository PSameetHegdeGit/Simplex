from flask import *
from Simplex import *
from flask_cors import CORS

app = Flask(__name__)

CORS(app)



@app.route("/calculateSimplex/<data>")
def solver(data):
    print(data)

    # use below script inorder to convert data delivered in JSON format into a python native format (e.g. list)
    data = json.loads(data)


    return simplexSolver(data)



# Put your app in here.

from flask import Flask, request
import operations

app = Flask(__name__)

functions = {
    "add" : operations.add,
    "sub" : operations.sub,
    "mult" : operations.mult,
    "div" : operations.div
}


@app.route("/math/<function_request>")
def return_result(function_request):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = functions[f'{function_request}'](a,b)   

    return f"{result}"

    # if function_request == "add":
    #     result = operations.add(a,b)
    #     return f"{result}"
    
    # if function_request == "sub":
    #     result = operations.sub(a,b)
    #     return f"{result}"
    
    # if function_request == "mult":
    #     result = operations.mult(a,b)
    #     return f"{result}"
    
    # if function_request == "div":
    #     result = operations.div(a,b)
    #     return f"{result}"

# *******NOTES I actually did the method below second in an attempt to fix the test that wasn't passing - guessing this is a Flask version issue

# @app.route("/add")
# def return_addition():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = operations.add(a,b)
#     return f"{result}"

# @app.route("/sub")
# def return_subtraction():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = operations.sub(a,b)
#     return f"{result}"

# @app.route("/mult")
# def return_multiplication():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = operations.mult(a,b)
#     return f"{result}"

# @app.route("/div")
# def return_division():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = operations.div(a,b)
#     return f"{result}"

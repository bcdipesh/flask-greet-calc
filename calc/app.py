from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)


def perfom_operation(operation, request):
    a = int(request.args['a'])
    b = int(request.args['b'])

    if operation == 'add':
        return str(add(a, b))
    elif operation == 'sub':
        return str(sub(a, b))
    elif operation == 'mult':
        return str(mult(a, b))
    elif operation == 'div':
        return str(div(a, b))


@app.route('/add')
def add_number():
    return perfom_operation('add', request)


@app.route('/sub')
def sub_number():
    return perfom_operation('sub', request)


@app.route('/mult')
def mult_number():
    return perfom_operation('mult', request)


@app.route('/div')
def div_number():
    return perfom_operation('div', request)


@app.route('/math/<operation>')
def math_operation(operation):
    return perfom_operation(operation, request)

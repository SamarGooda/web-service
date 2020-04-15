# from flask import Flask
# from flask import request
# from request  import * 
# import jsonify
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Employees=[{'id': 0,
     'name': 'A Fire Upon the Deep',
     'salay': 'Vernor Vinge'},
    {'id': 1,
     'name': 'The Ones Who Walk Away From Omelas',
     'salay': 'Ursula K. Le Guin'},
    {'id': 2,
     'name': 'Dhalgren',
     'salay': 'Samuel R. Delany'}]




@app.route('/',methods=['GET'])
def home ():
  print (request.form)
  return "<h1>hellooooooooooooooooooo</h>"


@app.route('/employees',methods=['GET','POST'])
def employee():
    if request.method == 'POST':
        emp = {}
        emp.id = request.id
        emp.name = request.name
        emp.salary = request.salary
        Employees.append(emp)
        return jsonify(Employees)
    elif request.method=='GET':
        return jsonify(Employees)
#show all employee
@app.route('/employees/all', methods=['GET'])
def api_all():
    return jsonify(Employees)


# @app.route('/api/v1/resources/employees/<int:id>', methods=['GET'])
# def api_id():
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."

@app.route('/employees/<int:id>',methods=['GET','DELETE','put'])
def operation(id):
    if request.method == 'GET':
        return getEmp (id)
    elif request.method == 'put':
        return updateEmp (id)
    elif request.method == 'DELETE':
        return deleteEmp (id)

def getEmp (id):
    for emp in Employees:
        if emp['id'] == id:
            return jsonify (emp)
    return None



def updateEmp (id):
    for emp in Employees:
        if emp['id'] == id:
            emp['name'] = request.form ['name']
            emp['salary'] = request.form ['salary']
            return jsonify (emp)
    return None


def deleteEmp (id):
    for emp in Employees:
        if emp['id'] == id:
            print ("hhhhhhhhhhhhhhhhhhhhhhhhhh")
            Employees.remove(emp)
            return jsonify (emp)
    return None
app.run()














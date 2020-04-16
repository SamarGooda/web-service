# from flask import Flask
# from flask import request
# from request  import * 
# import jsonify
import flask
import sqlite3
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


@app.route('/employees/',methods=['POST'])
def employee():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        salary = request.form['salary']
        conn = sqlite3.connect('provider_db.db')
        cur = conn.cursor() 
        new_employees = cur.execute('INSERT into employees VALUES ('+id+','+"\'"+name+"\'"+','+"\'"+salary+"\'"+');')
        all_employees = cur.execute('SELECT * FROM employees;')
        conn.commit()
        print (cur.rowcount)
        conn.close() 
        return jsonify(all_employees)
     


#show all employee
@app.route('/employees/', methods=['GET'])
def api_all():
    conn = sqlite3.connect('provider_db.db')
    cur = conn.cursor()   
    all_employees = cur.execute('SELECT * FROM employees;').fetchall()
    conn.commit()
    print (cur.rowcount)
    conn.close()
    return jsonify(all_employees)


#show all employee without database 
# @app.route('/employees/all', methods=['GET'])
# def api_all():
#     return jsonify(Employees)


# @app.route('/api/v1/resources/employees/<int:id>', methods=['GET'])
# def api_id():
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."

@app.route('/employees/<int:id>',methods=['GET','DELETE','PUT'])
def operation(id):
    if request.method == 'GET':
        return getEmp (id)
    elif request.method == 'PUT':
        return updateEmp (id)
    elif request.method == 'DELETE':
        return deleteEmp (id)

def getEmp (id):
    # for emp in Employees:
    #     if emp['id'] == id:
     conn = sqlite3.connect('provider_db.db')
     cur = conn.cursor() 
     emp = cur.execute('SELECT * FROM employees where id ='+str(id)+';').fetchall()
     conn.close()  
     return jsonify (emp)
    



def updateEmp (id):
    # for emp in Employees:
    #     if emp['id'] == id:
    #         emp['name'] = request.form ['name']
    #         emp['salary'] = request.form ['salary']
    #         return jsonify (emp)
    # return None
    id = request.form['id']
    name = request.form['name']
    salary = request.form['salary']
    conn = sqlite3.connect('provider_db.db')
    cur = conn.cursor() 
    emp = cur.execute('UPDATE employees SET id='+str(id)+','+'name='+"\'"+name+"\'"+','+'salary='+"\'"+salary+"\'"+' WHERE id ='+"\'"+str(id)+"\'"+';')
    conn.commit()
    print (cur.rowcount)
    conn.close()  
    return jsonify (emp)


def deleteEmp (id):
    # for emp in Employees:
    #     if emp['id'] == id:
    #         Employees.remove(emp)
    #         return jsonify (emp)
    # return None
     conn = sqlite3.connect('provider_db.db')
     cur = conn.cursor() 
     emp = cur.execute('DELETE FROM employees where id ='+str(id)+';')
     conn.commit()
     conn.close()  
     return str(cur.rowcount)



app.run()














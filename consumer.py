import requests 

URL = "http://127.0.0.1:5000/employees"
r = requests.get(url = URL)
print("Get All Employees: \n" + str(r.json()))

URL = "http://127.0.0.1:5000/employees"
new_employee = {
	'id': 4, 
	'name': 'Ayman',
	'salary': 4000
}
r = requests.post(url = URL, data = new_employee)
print("Add new Employee: \n" + str(r.json()))

URL = "http://127.0.0.1:5000/employees/4"
r = requests.get(url = URL)
print("Get An Employees: \n" + str(r.json()))

URL = "http://127.0.0.1:5000/employees/3"
employee = {
	'name': 'Esraa',
	'salary': 2700
}
r = requests.put(url = URL, data = employee)
print("Edit An Employees: \n" + str(r.json()))

URL = "http://127.0.0.1:5000/employees/3"
r = requests.delete(url = URL)
print("Delete An Employees: \n" + str(r.json()))
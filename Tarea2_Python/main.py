from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Test12345@localhost/people"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#instanciamos la coneccion a la base de datos
db = SQLAlchemy(app)

#setiamos el Model / Mapeo de la tabla /Difinimos los atributos y sus caracteristicas
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False) # podemos usar unique=True para valores que no deben duplicarse

    def __repr__(self):
        return f'<Employee {self.name}>'

#Ruta para el get
@app.route('/employee', methods=['GET'])
#Metodo para mostrar todos los empleados en mi tabla.
def getEmployees():
    employees = Employee.query.all()
    employee_list = []
    for employee in employees:
        employee_data = {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email
        }
        employee_list.append(employee_data)
    return jsonify(employee_list), 200


# Ruta para el get by id
@app.route('/employee/<int:id>', methods=['GET'])
# Metodo para mostrar empleado por id
def getEmployeeById(id):
    employee = Employee.query.get(id)
    if employee:
        employee_data = {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email
        }
        return jsonify(employee_data), 200
    else:
        return jsonify({"error": "Employee not found"}), 404

# Ruta para ingresar un nuevo usuario
@app.route('/employee', methods=['POST'])
#metodo para ingresar un nuevo usuario
def createEmployee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], email=data['email'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({
        "id": new_employee.id,
        "name": new_employee.name,
        "email": new_employee.email
    }), 201

app.run()
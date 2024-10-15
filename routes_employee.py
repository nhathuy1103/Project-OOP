# routes_employee.py
from flask import Blueprint, jsonify, request
from models import Employee
from extensions import db  # Import db từ extensions.py

employee_bp = Blueprint('employee_bp', __name__)

# API thêm nhân viên
@employee_bp.route('/', methods=['POST'])
def create_employee():
    data = request.json
    new_employee = Employee(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        role=data['role'],
        hire_date=data['hire_date']
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.display_info()), 201

# API lấy danh sách nhân viên
@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.display_info() for employee in employees])

# API cập nhật thông tin nhân viên
@employee_bp.route('/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"message": "Employee not found"}), 404

    employee.name = data.get('name', employee.name)
    employee.email = data.get('email', employee.email)
    employee.phone = data.get('phone', employee.phone)
    employee.role = data.get('role', employee.role)
    db.session.commit()
    return jsonify({"message": "Employee updated successfully"}), 200

# API xóa nhân viên
@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"message": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"}), 200

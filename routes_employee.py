# routes_employee.py
from flask import Blueprint, jsonify, request
from models import Employee
from app import db

employee_bp = Blueprint('employee_bp', __name__)

# Thêm nhân viên mới
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
    return jsonify({"message": "Employee created successfully"}), 201

# Lấy danh sách nhân viên
@employee_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = []
    for employee in employees:
        emp_data = {
            'employee_id': employee.employee_id,
            'name': employee.name,
            'email': employee.email,
            'phone': employee.phone,
            'role': employee.role,
            'hire_date': employee.hire_date.strftime('%Y-%m-%d')
        }
        result.append(emp_data)
    return jsonify(result)

# Cập nhật thông tin nhân viên
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

# Xóa nhân viên
@employee_bp.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if not employee:
        return jsonify({"message": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"}), 200

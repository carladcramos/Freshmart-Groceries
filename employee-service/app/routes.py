from flask import Blueprint, request, jsonify
from app.controller import create_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    employee = create_employee(data)
    return jsonify({"message": "Employee added successfully", "employee": employee.id}), 201

@employee_bp.route('/employees', methods=['GET'])
def list_employees():
    employees = get_all_employees()
    return jsonify([{
        "id": emp.id,
        "full_name": emp.full_name,
        "date_of_birth": str(emp.date_of_birth),
        "address": emp.address,
        "phone": emp.phone,
        "email": emp.email,
        "emergency_contact_name": emp.emergency_contact_name,
        "emergency_contact_phone": emp.emergency_contact_phone
    } for emp in employees])

@employee_bp.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        return jsonify({
            "id": employee.id,
            "full_name": employee.full_name,
            "date_of_birth": str(employee.date_of_birth),
            "address": employee.address,
            "phone": employee.phone,
            "email": employee.email,
            "emergency_contact_name": employee.emergency_contact_name,
            "emergency_contact_phone": employee.emergency_contact_phone
        })
    return jsonify({"message": "Employee not found"}), 404

@employee_bp.route('/employees/<int:employee_id>', methods=['PUT'])
def modify_employee(employee_id):
    data = request.json
    employee = update_employee(employee_id, data)
    if employee:
        return jsonify({"message": "Employee updated successfully"})
    return jsonify({"message": "Employee not found"}), 404

@employee_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
def remove_employee(employee_id):
    if delete_employee(employee_id):
        return jsonify({"message": "Employee deleted successfully"})
    return jsonify({"message": "Employee not found"}), 404

from app.models import db, Employee

def create_employee(data):
    new_employee = Employee(
        full_name=data['full_name'],
        date_of_birth=data['date_of_birth'],
        address=data['address'],
        phone=data['phone'],
        email=data['email'],
        emergency_contact_name=data['emergency_contact_name'],
        emergency_contact_phone=data['emergency_contact_phone']
    )
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

def get_all_employees():
    return Employee.query.all()

def get_employee_by_id(employee_id):
    return Employee.query.get(employee_id)

def update_employee(employee_id, data):
    employee = Employee.query.get(employee_id)
    if employee:
        employee.full_name = data.get('full_name', employee.full_name)
        employee.date_of_birth = data.get('date_of_birth', employee.date_of_birth)
        employee.address = data.get('address', employee.address)
        employee.phone = data.get('phone', employee.phone)
        employee.email = data.get('email', employee.email)
        employee.emergency_contact_name = data.get('emergency_contact_name', employee.emergency_contact_name)
        employee.emergency_contact_phone = data.get('emergency_contact_phone', employee.emergency_contact_phone)
        db.session.commit()
        return employee
    return None

def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return True
    return False

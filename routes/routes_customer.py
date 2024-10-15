from flask import Blueprint, jsonify, request
from models.customer import Customer, CustomerVip, CustomerSilver
from extensions import db

customer_bp = Blueprint('customer_bp', __name__)

# API thêm khách hàng
@customer_bp.route('/', methods=['POST'])
def create_customer():
    data = request.json
    customer_type = data.get('customer_type', 'regular')
    if customer_type == 'vip':
        new_customer = CustomerVip(name=data['name'], email=data['email'], phone=data['phone'], address=data['address'], date_of_birth=data.get('date_of_birth'))
    elif customer_type == 'silver':
        new_customer = CustomerSilver(name=data['name'], email=data['email'], phone=data['phone'], address=data['address'], date_of_birth=data.get('date_of_birth'))
    else:
        new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'], address=data['address'], date_of_birth=data.get('date_of_birth'))

    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": f"{customer_type.capitalize()} customer created successfully"}), 201

# API lấy danh sách khách hàng
@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{
        **customer.display_info(),
        'discount': customer.get_discount()
    } for customer in customers])

@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    customer.name = data.get('name', customer.name)
    customer.email = data.get('email', customer.email)
    customer.phone = data.get('phone', customer.phone)
    customer.address = data.get('address', customer.address)
    customer.date_of_birth = data.get('date_of_birth', customer.date_of_birth)
    
    db.session.commit()
    return jsonify({"message": "Customer updated successfully"}), 200

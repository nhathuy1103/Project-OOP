from flask import Flask, request, jsonify
from models import User, Product, Customer, Order, OrderItem
from config import Session

app = Flask(__name__)
session = Session()

# API cho User
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password=data['password'])
    session.add(new_user)
    session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = session.query(User).all()
    return jsonify([user.__dict__ for user in users])

# API cho Product (Sản phẩm)
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], description=data['description'], stock_quantity=data['stock_quantity'])
    session.add(new_product)
    session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = session.query(Product).all()
    return jsonify([product.__dict__ for product in products])

# API cho Customer (Khách hàng)
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], address=data['address'], phone_number=data['phone_number'], email=data['email'])
    session.add(new_customer)
    session.commit()
    return jsonify({"message": "Customer added successfully"}), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = session.query(Customer).all()
    return jsonify([customer.__dict__ for customer in customers])

# API cho Order (Đơn hàng)
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_id = data['customer_id']
    order_items = data['order_items']

    order = Order(customer_id=customer_id)
    session.add(order)
    session.commit()  # Lưu đơn hàng để lấy order_id

    for item in order_items:
        product = session.query(Product).filter_by(product_id=item['product_id']).first()
        if product:
            order_item = OrderItem(order_id=order.order_id, product_id=product.product_id, quantity=item['quantity'])
            session.add(order_item)

    session.commit()
    return jsonify({"message": "Order created successfully", "order_id": order.order_id}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = session.query(Order).all()
    return jsonify([order.__dict__ for order in orders])

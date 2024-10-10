from flask import Blueprint, jsonify, request
from models import db, Product, Order

# Khởi tạo blueprint cho các route
api = Blueprint('api', __name__)

#route lấy danh sách tất cả sản phẩm 
@api.route('/get_all_products', methods=['GET'])
def get_products():
    """Lấy danh sách tất cả sản phẩm."""
    products = Product.query.all()
    return jsonify([{
        'product_id': p.product_id,
        'product_name': p.product_name,
        'price': str(p.price),
        'quantity': p.quantity,
        'description': p.description
    } for p in products])

#route tạo mới một sản phẩm
@api.route('/create_products', methods=['POST'])
def create_product():
    """Tạo mới một sản phẩm."""
    data = request.get_json()
    new_product = Product(
        product_name=data['product_name'],
        price=data['price'],
        quantity=data['quantity'],
        description=data.get('description', '')  # Mô tả sản phẩm có thể không có
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully!'}), 201

#route tạo mới một đơn hàng
@api.route('/create_order', methods=['POST'])
def create_order():
    """Tạo một đơn hàng mới."""
    data = request.get_json()
    print(data)
    
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({'error': 'Product not found!'}), 404

    new_order = Order(
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created successfully!'}), 201

#route lấy danh sách tất cả đơn hàng
@api.route('/get_all_orders', methods=['GET'])
def get_orders():
    """Lấy danh sách tất cả đơn hàng."""
    orders = Order.query.all()
    return jsonify([{
        'order_id': o.order_id,
        'product_id': o.product_id,
        'order_date': o.order_date.strftime("%Y-%m-%d %H:%M:%S"),  
        'quantity': o.quantity
    } for o in orders])

#route thử nghiệm cấu hình flask
@api.route('/', methods=['GET'])
def index():
    """Trang chính của API."""
    return jsonify({'message': 'Welcome to the API!'})

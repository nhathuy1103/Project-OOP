from flask import Blueprint, jsonify, request
from models import db, Product, Order

# Khởi tạo blueprint cho các route
api = Blueprint('api', __name__)

# Lớp ProductManager để quản lý các chức năng của sản phẩm
class ProductManager:
    @staticmethod
    def get_all_products():
        """Lấy danh sách tất cả sản phẩm."""
        products = Product.query.all()
        return [{
            'product_id': p.product_id,
            'product_name': p.product_name,
            'price': str(p.price),
            'quantity': p.quantity,
            'description': p.description
        } for p in products]

    @staticmethod
    def create_product(data):
        """Tạo mới một sản phẩm."""
        new_product = Product(
            product_name=data['product_name'],
            price=data['price'],
            quantity=data['quantity'],
            description=data.get('description', '')
        )
        db.session.add(new_product)
        db.session.commit()

    @staticmethod
    def update_product(product_id, data):
        """Cập nhật thông tin sản phẩm."""
        product = Product.query.get(product_id)
        if product:
            product.product_name = data.get('product_name', product.product_name)
            product.price = data.get('price', product.price)
            product.quantity = data.get('quantity', product.quantity)
            product.description = data.get('description', product.description)
            db.session.commit()

    @staticmethod
    def delete_product(product_id):
        """Xóa một sản phẩm."""
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()

# Lớp OrderManager để quản lý các chức năng của đơn hàng
class OrderManager:
    @staticmethod
    def create_order(data):
        """Tạo một đơn hàng mới."""
        product = Product.query.get(data['product_id'])
        if not product:
            return None, 'Product not found!'
        
        new_order = Order(
            product_id=data['product_id'],
            quantity=data['quantity']
        )
        db.session.add(new_order)
        db.session.commit()
        return new_order, None

    @staticmethod
    def get_all_orders():
        """Lấy danh sách tất cả đơn hàng."""
        orders = Order.query.all()
        return [{
            'order_id': o.order_id,
            'product_id': o.product_id,
            'order_date': o.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            'quantity': o.quantity
        } for o in orders]

    @staticmethod
    def update_order_status(order_id, status):
        """Cập nhật trạng thái đơn hàng."""
        order = Order.query.get(order_id)
        if order:
            order.status = status
            db.session.commit()

    @staticmethod
    def delete_order(order_id):
        """Xóa đơn hàng."""
        order = Order.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()

# API cho sản phẩm
@api.route('/get_all_products', methods=['GET'])
def get_products():
    """Route lấy danh sách tất cả sản phẩm."""
    return jsonify(ProductManager.get_all_products())

@api.route('/create_products', methods=['POST'])
def create_product():
    """Route tạo mới một sản phẩm."""
    data = request.get_json()
    ProductManager.create_product(data)
    return jsonify({'message': 'Product created successfully!'}), 201

@api.route('/update_product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Route cập nhật thông tin sản phẩm."""
    data = request.get_json()
    ProductManager.update_product(product_id, data)
    return jsonify({'message': 'Product updated successfully!'})

@api.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Route xóa một sản phẩm."""
    ProductManager.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully!'})

# API cho đơn hàng
@api.route('/create_order', methods=['POST'])
def create_order():
    """Route tạo mới một đơn hàng."""
    data = request.get_json()
    new_order, error = OrderManager.create_order(data)
    if error:
        return jsonify({'error': error}), 404
    return jsonify({'message': 'Order created successfully!'}), 201

@api.route('/get_all_orders', methods=['GET'])
def get_orders():
    """Route lấy danh sách tất cả đơn hàng."""
    return jsonify(OrderManager.get_all_orders())

@api.route('/update_order_status/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    """Route cập nhật trạng thái đơn hàng."""
    data = request.get_json()
    OrderManager.update_order_status(order_id, data['status'])
    return jsonify({'message': 'Order status updated successfully!'})

@api.route('/delete_order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Route xóa đơn hàng."""
    OrderManager.delete_order(order_id)
    return jsonify({'message': 'Order deleted successfully!'})



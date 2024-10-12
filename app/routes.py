from flask import Blueprint, request, jsonify
from app.models import OrderItem
from database import db

orderitem_bp = Blueprint('orderitem', __name__)

@orderitem_bp.route('/orderitem', methods=['POST'])
def create_order_item():
    data = request.get_json()
    order_item = OrderItem(
        order_id=data['order_id'],
        product_id=data['product_id'],
        quantity=data['quantity'],
        price=data['price']
    )
    db.session.add(order_item)
    db.session.commit()
    return jsonify(order_item.to_dict()), 201



@orderitem_bp.route('/orderitem/<int:id>', methods=['GET', 'PUT'])
def handle_order_item(id):
    if request.method == 'GET':
        order_item = OrderItem.query.get(id)
        if order_item is None:
            return jsonify({'error': 'Order item not found'}), 404
        return jsonify(order_item.to_dict()), 200

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        order_item = OrderItem.query.get(id)
        if order_item is None:
            return jsonify({'error': 'Order item not found'}), 404

        # Cập nhật và xác minh các trường nếu có trong dữ liệu
        if 'quantity' in data:
            try:
                order_item.quantity = int(data['quantity'])
            except (ValueError, TypeError):
                return jsonify({'error': 'Invalid quantity value'}), 400

        if 'price' in data:
            try:
                order_item.price = float(data['price'])
            except (ValueError, TypeError):
                return jsonify({'error': 'Invalid price value'}), 400

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Database error', 'message': str(e)}), 500

        return jsonify(order_item.to_dict()), 200
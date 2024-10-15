# routes_inventory.py
from flask import Blueprint, jsonify, request
from models import Inventory
from app import db
from datetime import datetime

inventory_bp = Blueprint('inventory_bp', __name__)

# Thêm sản phẩm vào kho
@inventory_bp.route('/', methods=['POST'])
def create_inventory():
    data = request.json
    new_inventory = Inventory(
        product_id=data['product_id'],
        quantity_in_stock=data['quantity_in_stock'],
        reorder_level=data['reorder_level'],
        last_updated=datetime.utcnow()
    )
    db.session.add(new_inventory)
    db.session.commit()
    return jsonify({"message": "Inventory created successfully"}), 201

# Lấy danh sách kho
@inventory_bp.route('/', methods=['GET'])
def get_inventories():
    inventories = Inventory.query.all()
    result = []
    for inventory in inventories:
        inv_data = {
            'inventory_id': inventory.inventory_id,
            'product_id': inventory.product_id,
            'quantity_in_stock': inventory.quantity_in_stock,
            'reorder_level': inventory.reorder_level,
            'last_updated': inventory.last_updated.strftime('%Y-%m-%d %H:%M:%S')
        }
        result.append(inv_data)
    return jsonify(result)

# Cập nhật tồn kho
@inventory_bp.route('/<int:inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    data = request.json
    inventory = Inventory.query.get(inventory_id)
    if not inventory:
        return jsonify({"message": "Inventory not found"}), 404

    inventory.quantity_in_stock = data.get('quantity_in_stock', inventory.quantity_in_stock)
    inventory.reorder_level = data.get('reorder_level', inventory.reorder_level)
    inventory.last_updated = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "Inventory updated successfully"}), 200

# Xóa sản phẩm khỏi kho
@inventory_bp.route('/<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    inventory = Inventory.query.get(inventory_id)
    if not inventory:
        return jsonify({"message": "Inventory not found"}), 404

    db.session.delete(inventory)
    db.session.commit()
    return jsonify({"message": "Inventory deleted successfully"}), 200

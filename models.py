# models.py
from app import db

class Employee(db.Model):
    __tablename__ = 'Employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    # Các phương thức khác (nếu cần)

class Inventory(db.Model):
    __tablename__ = 'Inventory'
    inventory_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    reorder_level = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)


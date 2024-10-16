from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

##################################################################################################################################
class Customer(db.Model):
    __tablename__ = 'Customer'

    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    address = db.Column(db.Text, nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)

    def __init__(self, name, email, phone=None, address=None, date_of_birth=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.date_of_birth = date_of_birth

##################################################################################################################################
class Employees(db.Model):
    __tablename__ = 'Employees'

    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, email, phone, role, hire_date):
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role
        self.hire_date = hire_date

##################################################################################################################################
class Products(db.Model):
    __tablename__ = 'Products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, product_name, price, quantity, description=None):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.description = description

##################################################################################################################################
class Orders(db.Model):
    __tablename__ = 'Orders'

    order_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customer.customer_id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('Employees.employee_id'), nullable=True)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    product = db.relationship('Products', backref='orders')
    customer = db.relationship('Customer', backref='orders')
    employee = db.relationship('Employees', backref='orders')

    def __init__(self, product_id, customer_id, employee_id, quantity):
        self.product_id = product_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.quantity = quantity

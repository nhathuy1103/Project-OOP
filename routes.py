from flask import Blueprint, jsonify, request
from models import db, Products, Customer, Orders, Employees

# Khởi tạo blueprint cho các route
api = Blueprint('api', __name__)

##################################################################################################################################
# Lớp ProductManager để quản lý các chức năng của sản phẩm
class ProductManager:
    @staticmethod
    def create_product(data):
        """Thêm sản phẩm mới."""
        new_product = Products(
            product_name=data['product_name'],
            price=data['price'],
            quantity=data['quantity'],
            description=data.get('description')
        )
        db.session.add(new_product)
        db.session.commit()

    @staticmethod
    def delete_product(product_id):
        """Xóa một sản phẩm."""
        product = Products.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()

    @staticmethod
    def get_all_products():
        """Xem danh sách tất cả sản phẩm."""
        products = Products.query.all()
        return [{
            'product_id': p.product_id,
            'product_name': p.product_name,
            'price': str(p.price),
            'quantity': p.quantity,
            'description': p.description
        } for p in products]

    @staticmethod
    def search_products(keyword):
        """Tìm kiếm và lọc sản phẩm."""
        products = Products.query.filter(Products.product_name.like(f'%{keyword}%')).all()
        return [{
            'product_id': p.product_id,
            'product_name': p.product_name,
            'price': str(p.price),
            'quantity': p.quantity,
            'description': p.description
        } for p in products]

##################################################################################################################################
# Lớp CustomerManager để quản lý các chức năng của khách hàng
class CustomerManager:
    @staticmethod
    def create_customer(data):
        """Thêm khách hàng mới."""
        new_customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            address=data.get('address'),
            date_of_birth=data.get('date_of_birth')
        )
        db.session.add(new_customer)
        db.session.commit()

    @staticmethod
    def delete_customer(customer_id):
        """Xóa một khách hàng."""
        customer = Customer.query.get(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()

    @staticmethod
    def get_all_customers():
        """Xem danh sách khách hàng."""
        customers = Customer.query.all()
        return [{
            'customer_id': c.customer_id,
            'name': c.name,
            'email': c.email,
            'phone': c.phone,
            'address': c.address,
            'date_of_birth': c.date_of_birth.strftime("%Y-%m-%d") if c.date_of_birth else None
        } for c in customers]

    @staticmethod
    def get_order_history(customer_id):
        """Theo dõi lịch sử đơn hàng của khách hàng."""
        orders = Orders.query.filter_by(customer_id=customer_id).all()
        return [{
            'order_id': o.order_id,
            'product_id': o.product_id,
            'order_date': o.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            'quantity': o.quantity,
            'status': o.status
        } for o in orders]

##################################################################################################################################
# Lớp OrderManager để quản lý các chức năng của đơn hàng
class OrderManager:
    @staticmethod
    def create_order(data):
        """Tạo một đơn hàng mới."""
        product = Products.query.get(data['product_id'])  # Sử dụng Products
        if not product:
            return None, 'Product not found!'

        if product.quantity < data['quantity']:
            return None, 'Not enough quantity available!'

        # Tạo đơn hàng
        new_order = Orders(
            product_id=data['product_id'],
            quantity=data['quantity'],
            employee_id=data.get('employee_id'),  
            customer_id=data.get('customer_id')   
        )
        db.session.add(new_order)

        # Trừ số lượng sản phẩm
        product.quantity -= data['quantity']

        db.session.commit()
        return new_order, None

    @staticmethod
    def get_all_orders():
        """Xem danh sách tất cả đơn hàng."""
        orders = Orders.query.all()
        return [{
            'order_id': o.order_id,
            'product_id': o.product_id,
            'order_date': o.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            'quantity': o.quantity,
            'status': o.status
        } for o in orders]

    @staticmethod
    def update_order_status(order_id, status):
        """Cập nhật trạng thái đơn hàng."""
        order = Orders.query.get(order_id)
        if order:
            order.status = status
            db.session.commit()

    @staticmethod
    def delete_order(order_id):
        """Xóa đơn hàng."""
        order = Orders.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()

##################################################################################################################################
# Lớp EmployeeManager để quản lý các chức năng của nhân viên
class EmployeeManager:
    @staticmethod
    def create_employee(data):
        """Thêm nhân viên mới."""
        new_employee = Employees(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            role=data['role'],
            hire_date=data['hire_date']
        )
        db.session.add(new_employee)
        db.session.commit()

    @staticmethod
    def delete_employee(employee_id):
        """Xóa một nhân viên."""
        employee = Employees.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()

    @staticmethod
    def get_all_employees():
        """Xem danh sách nhân viên."""
        employees = Employees.query.all()
        return [{
            'employee_id': e.employee_id,
            'name': e.name,
            'email': e.email,
            'phone': e.phone,
            'role': e.role,
            'hire_date': e.hire_date.strftime("%Y-%m-%d")
        } for e in employees]

    @staticmethod
    def update_employee_role(employee_id, new_role):
        """Thay đổi Role cho nhân viên."""
        employee = Employees.query.get(employee_id)
        if employee:
            employee.role = new_role
            db.session.commit()

##################################################################################################################################
# API cho sản phẩm
@api.route('/create_product', methods=['POST'])
def create_product():
    data = request.get_json()
    ProductManager.create_product(data)
    return jsonify({'message': 'Product created successfully!'}), 201

@api.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    ProductManager.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully!'}), 200

@api.route('/products', methods=['GET'])
def get_products():
    products = ProductManager.get_all_products()
    return jsonify(products), 200

@api.route('/search_products/<keyword>', methods=['GET'])
def search_products(keyword):
    products = ProductManager.search_products(keyword)
    return jsonify(products), 200

##################################################################################################################################
# API cho khách hàng
@api.route('/create_customer', methods=['POST'])
def create_customer():
    data = request.get_json()
    CustomerManager.create_customer(data)
    return jsonify({'message': 'Customer created successfully!'}), 201

@api.route('/delete_customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    CustomerManager.delete_customer(customer_id)
    return jsonify({'message': 'Customer deleted successfully!'}), 200

@api.route('/customers', methods=['GET'])
def get_customers():
    customers = CustomerManager.get_all_customers()
    return jsonify(customers), 200

@api.route('/customer_order_history/<int:customer_id>', methods=['GET'])
def customer_order_history(customer_id):
    history = CustomerManager.get_order_history(customer_id)
    return jsonify(history), 200

##################################################################################################################################
# API cho đơn hàng
@api.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    order, error = OrderManager.create_order(data)
    if error:
        return jsonify({'error': error}), 400
    return jsonify({'message': 'Order created successfully!', 'order_id': order.order_id}), 201

@api.route('/orders', methods=['GET'])
def get_orders():
    orders = OrderManager.get_all_orders()
    return jsonify(orders), 200

@api.route('/update_order_status/<int:order_id>', methods=['PATCH'])
def update_order_status(order_id):
    status = request.get_json().get('status')
    OrderManager.update_order_status(order_id, status)
    return jsonify({'message': 'Order status updated successfully!'}), 200

@api.route('/delete_order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    OrderManager.delete_order(order_id)
    return jsonify({'message': 'Order deleted successfully!'}), 200

##################################################################################################################################
# API cho nhân viên
@api.route('/create_employee', methods=['POST'])
def create_employee():
    data = request.get_json()
    EmployeeManager.create_employee(data)
    return jsonify({'message': 'Employee created successfully!'}), 201

@api.route('/delete_employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    EmployeeManager.delete_employee(employee_id)
    return jsonify({'message': 'Employee deleted successfully!'}), 200

@api.route('/employees', methods=['GET'])
def get_employees():
    employees = EmployeeManager.get_all_employees()
    return jsonify(employees), 200

@api.route('/update_employee_role/<int:employee_id>', methods=['PATCH'])
def update_employee_role(employee_id):
    new_role = request.get_json().get('role')
    EmployeeManager.update_employee_role(employee_id, new_role)
    return jsonify({'message': 'Employee role updated successfully!'}), 200

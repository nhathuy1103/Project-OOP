from flask_sqlalchemy import SQLAlchemy

# Khởi tạo đối tượng SQLAlchemy
db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'Products'  # Tên bảng trong cơ sở dữ liệu

    # Định nghĩa các cột trong bảng
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    product_name = db.Column(db.String(100), nullable=False)  
    price = db.Column(db.Numeric(10, 2), nullable=False)  
    quantity = db.Column(db.Integer, nullable=False)  
    description = db.Column(db.Text) 

class Order(db.Model):
    __tablename__ = 'Orders'  # Tên bảng trong cơ sở dữ liệu

    # Định nghĩa các cột trong bảng
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'), nullable=False)  
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())  
    quantity = db.Column(db.Integer, nullable=False) 

    # Quan hệ với bảng Product
    product = db.relationship('Product', backref='orders')  # Cho phép truy cập thông tin sản phẩm từ đơn hàng
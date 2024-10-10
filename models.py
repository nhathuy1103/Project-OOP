from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Mô hình User đại diện cho bảng 'users'
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"

# Mô hình Product đại diện cho bảng 'products'
class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    stock_quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"

# Mô hình Customer đại diện cho bảng 'customers'
class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"

# Mô hình Order đại diện cho bảng 'orders'
class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    status = Column(String(50), default="Pending")

    customer = relationship("Customer")

    def __repr__(self):
        return f"<Order(id={self.order_id}, status={self.status})>"

# Mô hình OrderItem đại diện cho bảng 'order_items'
class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)

    product = relationship("Product")
    order = relationship("Order")

    def __repr__(self):
        return f"<OrderItem(product={self.product.name}, quantity={self.quantity})>"

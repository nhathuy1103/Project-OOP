import mysql.connector
from mysql.connector import Error
from abc import ABC, abstractmethod

# Lớp quản lý kết nối CSDL
class DatabaseConnection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '110303'  # Bạn nên thay bằng biến môi trường hoặc tệp cấu hình
        self.database = 'OOP'

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def close_connection(self, connection):
        if connection and connection.is_connected():
            connection.close()

# Lớp đại diện cho sản phẩm
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    # Phương thức để lưu sản phẩm vào cơ sở dữ liệu
    def save_to_db(self):
        db = DatabaseConnection()
        connection = db.connect()
        if connection is None:
            return
        try:
            cursor = connection.cursor()
            add_product_query = """
            INSERT INTO products (product_id, name, price, quantity)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name = VALUES(name),
                price = VALUES(price),
                quantity = VALUES(quantity)
            """
            cursor.execute(add_product_query, (
                self.product_id,
                self.name,
                self.price,
                self.quantity
            ))
            connection.commit()
        except Error as e:
            print(f"Error saving product to database: {e}")
        finally:
            cursor.close()
            db.close_connection(connection)

    # Phương thức để tải sản phẩm từ cơ sở dữ liệu
    @classmethod
    def load_from_db(cls, product_id):
        db = DatabaseConnection()
        connection = db.connect()
        if connection is None:
            return None
        try:
            cursor = connection.cursor()
            select_product_query = "SELECT * FROM products WHERE product_id = %s"
            cursor.execute(select_product_query, (product_id,))
            product_data = cursor.fetchone()
            if product_data:
                return cls(
                    product_id=product_data[0],
                    name=product_data[1],
                    price=product_data[2],
                    quantity=product_data[3]
                )
            else:
                print(f"No product found with ID: {product_id}")
                return None
        except Error as e:
            print(f"Error loading product from database: {e}")
            return None
        finally:
            cursor.close()
            db.close_connection(connection)

# Lớp Customer để quản lý khách hàng
class Customer:
    def __init__(self, customer_id, name, address, phone_number):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

# Lớp OrderItem để quản lý từng sản phẩm trong đơn hàng
class OrderItem:
    def __init__(self, product, quantity):
        self.__product = product  # Đối tượng sản phẩm
        self.__quantity = quantity  # Số lượng sản phẩm

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_total_price(self):
        return self.__product.price * self.__quantity

    def display_item(self):
        return f"{self.__product.name}: {self.__quantity} x {self.__product.price} = {self.get_total_price()}"

# Lớp Order để quản lý đơn hàng
class Order:
    def __init__(self, order_id, customer, order_items):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_items = order_items  # Danh sách các OrderItem
        self.__total_price = self.calculate_total()

    def calculate_total(self):
        total = 0
        for item in self.__order_items:
            total += item.get_total_price()
        return total

    def display_order(self):
        item_details = "\n".join([item.display_item() for item in self.__order_items])
        return f"Order ID: {self.__order_id}\nCustomer: {self.__customer.get_name()}\nItems:\n{item_details}\nTotal Price: {self.__total_price}"

    def get_order_id(self):
        return self.__order_id

    def get_total_price(self):
        return self.__total_price

    def get_customer(self):
        return self.__customer

    def get_order_items(self):
        return self.__order_items

# Lớp OrderManager để quản lý đơn hàng và tương tác với cơ sở dữ liệu
class OrderManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_orders_table(self):
        connection = self.db.connect()
        if connection is None:
            return
        try:
            cursor = connection.cursor()
            create_orders_table_query = """
            CREATE TABLE IF NOT EXISTS orders (
                order_id VARCHAR(255) PRIMARY KEY,
                customer_id VARCHAR(255),
                total_price FLOAT,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            );
            """
            cursor.execute(create_orders_table_query)
            connection.commit()

            create_order_items_table_query = """
            CREATE TABLE IF NOT EXISTS order_items (
                order_item_id INT AUTO_INCREMENT PRIMARY KEY,
                order_id VARCHAR(255),
                product_id VARCHAR(255),
                quantity INT,
                price FLOAT,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            );
            """
            cursor.execute(create_order_items_table_query)
            connection.commit()
        except Error as e:
            print(f"Error creating orders tables: {e}")
        finally:
            cursor.close()
            self.db.close_connection(connection)

    def add_order_to_db(self, order):
        connection = self.db.connect()
        if connection is None:
            return
        try:
            cursor = connection.cursor()
            add_order_query = """
            INSERT INTO orders (order_id, customer_id, total_price)
            VALUES (%s, %s, %s)
            """
            cursor.execute(add_order_query, (
                order.get_order_id(),
                order.get_customer().get_customer_id(),
                order.get_total_price()
            ))

            add_order_item_query = """
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s)
            """
            for item in order.get_order_items():
                cursor.execute(add_order_item_query, (
                    order.get_order_id(),
                    item.get_product().product_id,
                    item.get_quantity(),
                    item.get_product().price
                ))
            connection.commit()
            print("Order and items added to database successfully.")
        except Error as e:
            print(f"Error adding order to database: {e}")
        finally:
            cursor.close()
            self.db.close_connection(connection)

    def display_order_items_from_db(self, order_id):
        connection = self.db.connect()
        if connection is None:
            return
        try:
            cursor = connection.cursor()
            query = """
            SELECT product_id, quantity, price FROM order_items WHERE order_id = %s
            """
            cursor.execute(query, (order_id,))
            items = cursor.fetchall()
            print(f"Items for Order ID {order_id}:")
            for item in items:
                print(f"Product ID: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")
        except Error as e:
            print(f"Error retrieving order items: {e}")
        finally:
            cursor.close()
            self.db.close_connection(connection)

# Hàm để thêm đơn hàng
def add_order():
    order_id = input("Enter Order ID: ")
    customer_id = input("Enter Customer ID: ")

    # Tải thông tin khách hàng từ cơ sở dữ liệu
    # Bạn cần implement hàm load_customer_from_db trong CustomerManager
    customer_manager = CustomerManager()
    customer = customer_manager.load_customer_from_db(customer_id)
    if not customer:
        print("Customer not found.")
        return

    order_items = []
    while True:
        product_id = input("Enter Product ID (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        product = Product.load_from_db(product_id)
        if product:
            quantity = int(input(f"Enter quantity (available: {product.quantity}): "))
            if quantity > product.quantity:
                print("Not enough stock.")
                continue
            order_item = OrderItem(product, quantity)
            order_items.append(order_item)
        else:
            print("Product not found.")

    if order_items:
        order = Order(order_id, customer, order_items)
        order_manager = OrderManager()
        order_manager.add_order_to_db(order)
        print("Order created successfully.")
        print(order.display_order())
    else:
        print("No items in order.")

# Menu chính để tương tác với hệ thống
def main_menu():
    while True:
        print("\n1. Add Order")
        print("2. Show Order Items")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_order()
        elif choice == '2':
            order_id = input("Enter Order ID to display: ")
            order_manager = OrderManager()
            order_manager.display_order_items_from_db(order_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Lớp CustomerManager để quản lý khách hàng
class CustomerManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_customers_table(self):
        connection = self.db.connect()
        if connection is None:
            return
        try:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address VARCHAR(255),
                phone_number VARCHAR(20)
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
        except Error as e:
            print(f"Error creating customers table: {e}")
        finally:
            cursor.close()
            self.db.close_connection(connection)

    def load_customer_from_db(self, customer_id):
        connection = self.db.connect()
        if connection is None:
            return None
        try:
            cursor = connection.cursor()
            select_customer_query = "SELECT * FROM customers WHERE customer_id = %s"
            cursor.execute(select_customer_query, (customer_id,))
            customer_data = cursor.fetchone()
            if customer_data:
                return Customer(
                    customer_id=customer_data[0],
                    name=customer_data[1],
                    address=customer_data[2],
                    phone_number=customer_data[3]
                )
            else:
                return None
        except Error as e:
            print(f"Error loading customer from database: {e}")
            return None
        finally:
            cursor.close()
            self.db.close_connection(connection)

if __name__ == "__main__":
    # Tạo bảng nếu chưa tồn tại
    product_manager = Product('','','',0)
    order_manager = OrderManager()
    customer_manager = CustomerManager()

    # Tạo bảng sản phẩm
    connection = DatabaseConnection().connect()
    if connection:
        try:
            cursor = connection.cursor()
            create_products_table_query = """
            CREATE TABLE IF NOT EXISTS products (
                product_id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price FLOAT NOT NULL,
                quantity INT NOT NULL
            );
            """
            cursor.execute(create_products_table_query)
            connection.commit()
        except Error as e:
            print(f"Error creating products table: {e}")
        finally:
            cursor.close()
            connection.close()

    # Tạo bảng khách hàng
    customer_manager.create_customers_table()
    # Tạo bảng đơn hàng
    order_manager.create_orders_table()

    main_menu()

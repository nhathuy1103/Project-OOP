class Employee:
    def __init__(self, employee_id=None, name=None, email=None, phone=None, role=None, hire_date=None):
        self._employee_id = employee_id
        self._name = name
        self._email = email
        self._phone = phone
        self._role = role
        self._hire_date = hire_date

    # Getter và Setter cho name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = name

    # Getter và Setter cho email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email:
            self._email = email

    # Getter cho employee_id (read-only)
    @property
    def employee_id(self):
        return self._employee_id

    # Phương thức hiển thị thông tin nhân viên
    def display_info(self):
        return {
            'employee_id': self._employee_id,
            'name': self._name,
            'email': self._email,
            'phone': self._phone,
            'role': self._role,
            'hire_date': self._hire_date
        }


class Inventory:
    def __init__(self, inventory_id=None, product_id=None, quantity_in_stock=None, reorder_level=None, last_updated=None):
        # Encapsulation - Sử dụng protected attributes
        self._inventory_id = inventory_id
        self._product_id = product_id
        self._quantity_in_stock = quantity_in_stock
        self._reorder_level = reorder_level
        self._last_updated = last_updated

    # Getter và Setter cho quantity_in_stock
    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, new_quantity):
        if new_quantity >= 0:
            self._quantity_in_stock = new_quantity

    # Getter và Setter cho reorder_level
    @property
    def reorder_level(self):
        return self._reorder_level

    @reorder_level.setter
    def reorder_level(self, level):
        if level > 0:
            self._reorder_level = level

    # Phương thức kiểm tra xem có cần đặt hàng lại không
    def needs_reorder(self):
        return self._quantity_in_stock < self._reorder_level

    # Phương thức hiển thị thông tin kho
    def display_inventory(self):
        return {
            'inventory_id': self._inventory_id,
            'product_id': self._product_id,
            'quantity_in_stock': self._quantity_in_stock,
            'reorder_level': self._reorder_level,
            'last_updated': self._last_updated
        }

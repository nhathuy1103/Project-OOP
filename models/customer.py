from extensions import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)

    # Phương thức hiển thị thông tin khách hàng
    def display_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'date_of_birth': self.date_of_birth,
            'loyalty_type': self.__class__.__name__
        }

    def get_discount(self):
        return 0  # Khách hàng mặc định không có ưu đãi

class CustomerVip(Customer):
    def get_discount(self):
        return 20  # Giảm giá 20% cho khách hàng VIP

class CustomerSilver(Customer):
    def get_discount(self):
        return 10  # Giảm giá 10% cho khách hàng Bạc

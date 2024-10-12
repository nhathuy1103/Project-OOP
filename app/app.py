# Trong file app.py
from flask import Flask
from orderitem_routes import orderitem_bp  # Đảm bảo đường dẫn đúng tới file chứa Blueprint

app = Flask(__name__)

# Đăng ký Blueprint với url_prefix
app.register_blueprint(orderitem_bp, url_prefix='/api')  # Nếu có sử dụng url_prefix

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from extensions import db  # Import db từ extensions.py, không import routes ở đây

def create_app():
    app = Flask(__name__)

    # Cấu hình kết nối đến cơ sở dữ liệu MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql12736967:4LIpGVNBym@sql12.freemysqlhosting.net/sql12736967'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo db với app
    db.init_app(app)

    # Import các route sau khi khởi tạo app
    from routes_employee import employee_bp
    from routes_inventory import inventory_bp

    # Đăng ký các blueprint
    app.register_blueprint(employee_bp, url_prefix='/employees')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')

    return app

if __name__ == '__main__':
    app = create_app()  # Tạo ứng dụng
    app.run(debug=True)

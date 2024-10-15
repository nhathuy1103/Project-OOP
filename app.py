from flask import Flask
from extensions import db
from routes.routes_customer import customer_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql12736967:4LIpGVNBym@sql12.freemysqlhosting.net/sql12736967'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Khởi tạo db với app
    db.init_app(app)

    # Đăng ký các blueprint
    app.register_blueprint(customer_bp, url_prefix='/customers')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

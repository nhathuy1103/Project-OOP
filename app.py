from flask import Flask
from config import Config
from models import db
from routes import api  

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Sử dụng app context để tạo bảng
with app.app_context():
    db.create_all()  

# Đăng ký blueprint cho các route
app.register_blueprint(api, url_prefix='/api')

#in ra các route hiện có 
with app.app_context():
    print(app.url_map)  


if __name__ == '__main__':
    app.run(debug=True)  # Chạy ứng dụng Flask

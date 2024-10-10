from flask import Flask
from models import Base
from config import engine
import routes  # Import các routes từ routes.py

app = routes.app  # Khởi tạo ứng dụng Flask từ routes.py

# Tạo bảng trong cơ sở dữ liệu nếu chưa tồn tại
Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

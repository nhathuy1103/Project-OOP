# Giải thích ý nghĩa từng file
     
- app.py         #Nơi khởi động Flask server và định nghĩa các route (đường dẫn) của API.
     
- models.py      #Chứa định nghĩa các mô hình (models) tương ứng với các bảng trong cơ sở dữ liệu MySQL. Các models này được định nghĩa theo cú pháp của SQLAlchemy.
    
 - config.py      #Chứa cấu hình cho ứng dụng thông tin kết nối tới cơ sở dữ liệu MySQL
    
 - routes.py      #Chứa định nghĩa các route và logic xử lý API
    
- requirements.txt  #Các thư viện cần thiết để chạy chương trình
    
- Database_Source.txt  #DDL của database phòng trường hợp mất host online
    
- ER_Diagram.png  #Sơ đồ ER của database
    
- Check_api.txt  #Địa chỉ và cú pháp check api (sử dụng postman giao thức http)

- _pycache_ #thư mục chứa file bytecode của Python để giúp chương trình chạy nhanh hơn.khi chạy app.py sẽ tự động đẻ ra file này (không ảnh hưởng gì tới các chức năng của chương trình)
    

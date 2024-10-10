from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cấu hình kết nối MySQL
DATABASE_URI = 'mysql+pymysql://root:110303@localhost/dataoop'  # Thay thông tin đăng nhập và tên database phù hợp

# Khởi tạo engine và session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

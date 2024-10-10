class Config:
    # Thông tin cấu hình kết nối đến MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:none@localhost/quan_ly_ban_le'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    



# Kiểm tra kết nối (thay đổi các tham số để test trên máy mình nhé)
'''
import pymysql  # Thêm dòng này để import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='none',  # Thay 'none' bằng mật khẩu đúng nếu cần
        db='quan_ly_ban_le'
    )
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Đã kết nối thành công! Phiên bản MySQL: {version[0]}") 

except Exception as e:
    print(f"Kết nối thất bại: {str(e)}")

finally:
    if 'connection' in locals() and connection:  # Kiểm tra xem connection đã được định nghĩa
        connection.close()
'''
class Config:
    # Thông tin cấu hình kết nối đến MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql12736967:4LIpGVNBym@sql12.freemysqlhosting.net/sql12736967'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
# Kiểm tra kết nối
import pymysql  # Thêm dòng này để import pymysql

try:
    connection = pymysql.connect(
        host='sql12.freemysqlhosting.net',
        user='sql12736967',
        password='4LIpGVNBym',  # Thay 'none' bằng mật khẩu đúng nếu cần
        db='sql12736967',
        port=3306  # Cổng kết nối mặc định cho MySQL
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
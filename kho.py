# Lớp Kho
class Kho:
    def __init__(self):
        # Sử dụng dictionary để lưu trữ mã sản phẩm và thông tin liên quan
        self.__danh_sach_san_pham = {}

    # Phương thức nhập hàng
    def nhap_hang(self, san_pham, so_luong):
        ma_sp = san_pham.get_ma_san_pham()
        if ma_sp in self.__danh_sach_san_pham:
            self.__danh_sach_san_pham[ma_sp]['so_luong'] += so_luong
        else:
            self.__danh_sach_san_pham[ma_sp] = {
                'san_pham': san_pham,
                'so_luong': so_luong
            }
        print(f"Đã nhập {so_luong} sản phẩm mã {ma_sp} vào kho.")

    # Phương thức xuất hàng
    def xuat_hang(self, san_pham, so_luong):
        ma_sp = san_pham.get_ma_san_pham()
        if ma_sp in self.__danh_sach_san_pham:
            so_luong_hien_tai = self.__danh_sach_san_pham[ma_sp]['so_luong']
            if so_luong_hien_tai >= so_luong:
                self.__danh_sach_san_pham[ma_sp]['so_luong'] -= so_luong
                print(f"Đã xuất {so_luong} sản phẩm mã {ma_sp} khỏi kho.")
            else:
                print("Không đủ số lượng trong kho để xuất.")
        else:
            print("Sản phẩm không tồn tại trong kho.")

    # Phương thức kiểm tra tồn kho
    def kiem_tra_ton_kho(self, san_pham):
        ma_sp = san_pham.get_ma_san_pham()
        if ma_sp in self.__danh_sach_san_pham:
            return self.__danh_sach_san_pham[ma_sp]['so_luong']
        else:
            return 0

    # Phương thức tìm kiếm sản phẩm
    def tim_kiem_san_pham(self, ma_san_pham):
        return ma_san_pham in self.__danh_sach_san_pham

    # Phương thức cập nhật thông tin sản phẩm
    def cap_nhat_thong_tin_san_pham(self, san_pham):
        ma_sp = san_pham.get_ma_san_pham()
        if ma_sp in self.__danh_sach_san_pham:
            self.__danh_sach_san_pham[ma_sp]['san_pham'] = san_pham
            print(f"Đã cập nhật thông tin sản phẩm mã {ma_sp}.")
        else:
            print("Sản phẩm không tồn tại trong kho.")

    # Phương thức báo cáo tồn kho
    def bao_cao_ton_kho(self):
        print("----- Báo cáo tồn kho -----")
        if not self.__danh_sach_san_pham:
            print("Kho hiện đang trống.")
        else:
            for ma_sp, info in self.__danh_sach_san_pham.items():
                san_pham = info['san_pham']
                so_luong = info['so_luong']
                print(f"Mã sản phẩm: {ma_sp}, Tên: {san_pham.ten}, Số lượng: {so_luong}")
        print("---------------------------")

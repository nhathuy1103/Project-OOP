class NhanVien:
    """Lớp đại diện cho một nhân viên trong hệ thống quản lý bán lẻ."""

    def __init__(self, ma_nhan_vien, ten, vai_tro, luong, email, so_dien_thoai, dia_chi):
        self._ma_nhan_vien = ma_nhan_vien  # Thuộc tính riêng tư, chỉ đọc
        self.ten = ten
        self.vai_tro = vai_tro
        self.luong = luong
        self.email = email
        self.so_dien_thoai = so_dien_thoai
        self.dia_chi = dia_chi

    # Thuộc tính chỉ đọc cho ma_nhan_vien
    @property
    def ma_nhan_vien(self):
        return self._ma_nhan_vien

    # Thuộc tính ten với getter và setter
    @property
    def ten(self):
        return self._ten

    @ten.setter
    def ten(self, gia_tri):
        if not gia_tri.strip():
            raise ValueError("Tên không được để trống.")
        self._ten = gia_tri.strip()

    # Thuộc tính vai_tro với getter và setter
    @property
    def vai_tro(self):
        return self._vai_tro

    @vai_tro.setter
    def vai_tro(self, gia_tri):
        vai_tro_hop_le = {'Nhân viên bán hàng', 'Quản lý', 'Nhân viên kho', 'Thu ngân'}
        if gia_tri not in vai_tro_hop_le:
            raise ValueError(f"Vai trò phải là một trong các giá trị: {vai_tro_hop_le}.")
        self._vai_tro = gia_tri

    # Thuộc tính luong với getter và setter
    @property
    def luong(self):
        return self._luong

    @luong.setter
    def luong(self, gia_tri):
        if gia_tri < 0:
            raise ValueError("Lương không được âm.")
        self._luong = gia_tri

    # Thuộc tính email với getter và setter
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, gia_tri):
        if "@" not in gia_tri or not gia_tri.strip():
            raise ValueError("Địa chỉ email không hợp lệ.")
        self._email = gia_tri.strip()

    # Thuộc tính so_dien_thoai với getter và setter
    @property
    def so_dien_thoai(self):
        if self._so_dien_thoai.startswith('+'):
            return self._so_dien_thoai
        else:
            return '+84' + self._so_dien_thoai  # Mặc định mã quốc gia Việt Nam

    @so_dien_thoai.setter
    def so_dien_thoai(self, gia_tri):
        if not gia_tri.isdigit() or len(gia_tri) < 9:
            raise ValueError("Số điện thoại không hợp lệ.")
        self._so_dien_thoai = gia_tri

    # Thuộc tính dia_chi với getter và setter
    @property
    def dia_chi(self):
        return self._dia_chi

    @dia_chi.setter
    def dia_chi(self, gia_tri):
        if not gia_tri.strip():
            raise ValueError("Địa chỉ không được để trống.")
        self._dia_chi = gia_tri.strip()

    # Phương thức tính lương hàng năm
    def tinh_luong_hang_nam(self):
        """Tính lương hàng năm dựa trên lương tháng."""
        return self.luong * 12

    # Phương thức lấy thông tin liên hệ
    def lay_thong_tin_lien_he(self):
        """Trả về thông tin liên hệ của nhân viên."""
        return {
            'Email': self.email,
            'Số điện thoại': self.so_dien_thoai,
            'Địa chỉ': self.dia_chi
        }

    # Phương thức chuyển đổi đối tượng thành dictionary
    def to_dict(self):
        """Chuyển đổi dữ liệu nhân viên thành dictionary."""
        return {
            'Mã nhân viên': self.ma_nhan_vien,
            'Tên': self.ten,
            'Vai trò': self.vai_tro,
            'Lương': self.luong,
            'Email': self.email,
            'Số điện thoại': self.so_dien_thoai,
            'Địa chỉ': self.dia_chi
        }

    # Phương thức hiển thị thông tin đối tượng
    def __str__(self):
        return f"Nhân viên[{self.ma_nhan_vien}]: {self.ten}, {self.vai_tro}"

    def __repr__(self):
        return (f"NhanVien(ma_nhan_vien={self.ma_nhan_vien}, ten='{self.ten}', "
                f"vai_tro='{self.vai_tro}', luong={self.luong})")
    

class NhanVienBanHang(NhanVien):
    """Lớp đại diện cho nhân viên bán hàng, kế thừa từ NhanVien."""

    def __init__(self, ma_nhan_vien, ten, luong, email, so_dien_thoai, dia_chi, muc_tieu_ban_hang):
        super().__init__(ma_nhan_vien, ten, 'Nhân viên bán hàng', luong, email, so_dien_thoai, dia_chi)
        self.muc_tieu_ban_hang = muc_tieu_ban_hang
        self.doanh_so_dat_duoc = 0  # Doanh số đạt được

    # Phương thức cập nhật doanh số
    def cap_nhat_doanh_so(self, so_tien):
        if so_tien < 0:
            raise ValueError("Doanh số không được âm.")
        self.doanh_so_dat_duoc += so_tien

    # Phương thức tính hoa hồng
    def tinh_hoa_hong(self):
        ty_le_hoa_hong = 0.05  # Hoa hồng 5%
        return self.doanh_so_dat_duoc * ty_le_hoa_hong
    

    
class QuanLy(NhanVien):
    """Lớp đại diện cho quản lý, kế thừa từ NhanVien."""

    def __init__(self, ma_nhan_vien, ten, luong, email, so_dien_thoai, dia_chi, phong_ban):
        super().__init__(ma_nhan_vien, ten, 'Quản lý', luong, email, so_dien_thoai, dia_chi)
        self.phong_ban = phong_ban
        self.thanh_vien_nhom = []

    # Phương thức thêm thành viên vào nhóm
    def them_thanh_vien(self, nhan_vien):
        if not isinstance(nhan_vien, NhanVien):
            raise ValueError("Thành viên phải là đối tượng NhanVien.")
        self.thanh_vien_nhom.append(nhan_vien)

    # Phương thức phê duyệt đơn nghỉ phép
    def phe_duyet_nghi_phep(self, nhan_vien, so_ngay):
        print(f"Quản lý {self.ten} đã phê duyệt {so_ngay} ngày nghỉ cho {nhan_vien.ten}.")

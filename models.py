class Phong:
    def __init__(self, ma_phong, ten_phong, gia_co_ban):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong
        self.gia_co_ban = gia_co_ban
        self._trang_thai = "Trống"  # thuộc tính protected

    def get_trang_thai(self):
        return self._trang_thai

    def set_trang_thai(self, trang_thai):
        if trang_thai in ["Trống", "Đã thuê"]:
            self._trang_thai = trang_thai
        else:
            raise ValueError("Trạng thái không hợp lệ")


class PhongThuong(Phong):
    def tinh_tien(self, so_ngay):
        return self.gia_co_ban * so_ngay


class PhongVIP(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban, phi_don_dep, phi_minibar):
        super().__init__(ma_phong, ten_phong, gia_co_ban)
        self.phi_don_dep = phi_don_dep
        self.phi_minibar = phi_minibar

    def tinh_tien(self, so_ngay):
        return self.gia_co_ban * so_ngay + self.phi_don_dep + self.phi_minibar


class KhachHang:
    def __init__(self, ma_khach, ten, so_cccd):
        self.ma_khach = ma_khach
        self.ten = ten
        self.so_cccd = so_cccd


class PhieuThue:
    def __init__(self, khach_hang, phong, so_ngay):
        self.khach_hang = khach_hang
        self.phong = phong
        self.so_ngay = so_ngay
        self.tong_tien = phong.tinh_tien(so_ngay)

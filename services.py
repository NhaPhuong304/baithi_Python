from models import PhongThuong, PhongVIP, KhachHang, PhieuThue
from handler import save_data, load_data

class QuanLyKhachSan:
    def __init__(self):
        data = load_data()
        self.danh_sach_phong = []
        self.danh_sach_phieu = []
        self.doanh_thu = 0

        # Khởi tạo lại từ file JSON
        for p in data["phongs"]:
            if p["loai"] == "PhongThuong":
                phong = PhongThuong(p["ma_phong"], p["ten_phong"], p["gia_co_ban"])
            else:
                phong = PhongVIP(p["ma_phong"], p["ten_phong"], p["gia_co_ban"], p["phi_don_dep"], p["phi_minibar"])
            phong.set_trang_thai(p["trang_thai"])
            self.danh_sach_phong.append(phong)

        for ph in data["phieus"]:
            kh = KhachHang(ph["ma_khach"], ph["ten"], ph["so_cccd"])
            phong = next((x for x in self.danh_sach_phong if x.ma_phong == ph["ma_phong"]), None)
            if phong:
                phieu = PhieuThue(kh, phong, ph["so_ngay"])
                self.danh_sach_phieu.append(phieu)
                self.doanh_thu += phieu.tong_tien

    def them_phong(self, phong):
        self.danh_sach_phong.append(phong)

    def dat_phong(self, ma_phong, khach_hang, so_ngay):
        phong = next((p for p in self.danh_sach_phong if p.ma_phong == ma_phong), None)
        if not phong:
            raise ValueError("Phòng không tồn tại")
        if phong.get_trang_thai() == "Đã thuê":
            raise ValueError("Phòng đã được thuê")
        phong.set_trang_thai("Đã thuê")
        phieu = PhieuThue(khach_hang, phong, so_ngay)
        self.danh_sach_phieu.append(phieu)
        return phieu

    def tra_phong(self, ma_phong):
        phieu = next((ph for ph in self.danh_sach_phieu if ph.phong.ma_phong == ma_phong), None)
        if not phieu:
            raise ValueError("Không tìm thấy phiếu thuê cho phòng này")
        tong_tien = phieu.tong_tien
        phieu.phong.set_trang_thai("Trống")
        self.doanh_thu += tong_tien
        self.danh_sach_phieu.remove(phieu)
        return tong_tien

    def bao_cao(self):
        so_phong_trong = sum(1 for p in self.danh_sach_phong if p.get_trang_thai() == "Trống")
        return {"doanh_thu": self.doanh_thu, "phong_trong": so_phong_trong}

    def save(self):
        save_data(self.danh_sach_phong, self.danh_sach_phieu)


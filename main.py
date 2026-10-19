from models import PhongThuong, PhongVIP, KhachHang
from services import QuanLyKhachSan

def main():
    qlks = QuanLyKhachSan()

    while True:
        print("\n===== QUẢN LÝ KHÁCH SẠN =====")
        print("1. Hiển thị danh sách phòng")
        print("2. Thêm phòng mới")
        print("3. Đặt phòng")
        print("4. Trả phòng & Thanh toán")
        print("5. Xem báo cáo doanh thu")
        print("6. Thoát & Lưu dữ liệu")

        try:
            choice = int(input("Chọn chức năng: "))
        except ValueError:
            print("⚠️ Vui lòng nhập số hợp lệ!")
            continue

        if choice == 1:
            print("\n--- DANH SÁCH PHÒNG ---")
            for p in qlks.danh_sach_phong:
                print(f"{p.ma_phong} - {p.ten_phong} - Giá: {p.gia_co_ban} - Trạng thái: {p.get_trang_thai()}")

        elif choice == 2:
            loai = input("Loại phòng (Thuong/VIP): ")
            ma = input("Mã phòng: ")
            ten = input("Tên phòng: ")
            try:
                gia = int(input("Giá cơ bản: "))
            except ValueError:
                print("⚠️ Giá phải là số!")
                continue

            if loai.lower() == "vip":
                try:
                    phi_don_dep = int(input("Phí dọn dẹp: "))
                    phi_minibar = int(input("Phí minibar: "))
                except ValueError:
                    print("⚠️ Phí phải là số!")
                    continue
                phong = PhongVIP(ma, ten, gia, phi_don_dep, phi_minibar)
            else:
                phong = PhongThuong(ma, ten, gia)

            qlks.them_phong(phong)
            print("✅ Thêm phòng thành công!")

        elif choice == 3:
            ma_phong = input("Nhập mã phòng: ")
            ma_khach = input("Mã khách: ")
            ten = input("Tên khách: ")
            so_cccd = input("Số CCCD/CMND: ")
            try:
                so_ngay = int(input("Số ngày thuê: "))
            except ValueError:
                print("⚠️ Số ngày phải là số!")
                continue

            khach = KhachHang(ma_khach, ten, so_cccd)
            try:
                phieu = qlks.dat_phong(ma_phong, khach, so_ngay)
                print(f"✅ Đặt phòng thành công! Tổng tiền: {phieu.tong_tien}")
            except ValueError as e:
                print(f"⚠️ {e}")

        elif choice == 4:
            ma_phong = input("Nhập mã phòng cần trả: ")
            try:
                tong_tien = qlks.tra_phong(ma_phong)
                print(f"💰 Khách phải trả: {tong_tien}")
                print("✅ Trả phòng thành công!")
            except ValueError as e:
                print(f"⚠️ {e}")

        elif choice == 5:
            bc = qlks.bao_cao()
            print("\n--- BÁO CÁO DOANH THU ---")
            print(f"Tổng doanh thu: {bc['doanh_thu']}")
            print(f"Số phòng đang trống: {bc['phong_trong']}")

        elif choice == 6:
            qlks.save()
            print("💾 Dữ liệu đã được lưu. Thoát chương trình...")
            break

        else:
            print("⚠️ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()

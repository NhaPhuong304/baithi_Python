import json

def save_data(danh_sach_phong, danh_sach_phieu):
    data = {
        "phongs": [],
        "phieus": []
    }

    for p in danh_sach_phong:
        if isinstance(p, dict):
            data["phongs"].append(p)
        else:
            phong_data = {
                "ma_phong": p.ma_phong,
                "ten_phong": p.ten_phong,
                "gia_co_ban": p.gia_co_ban,
                "trang_thai": p.get_trang_thai(),
                "loai": p.__class__.__name__,
            }
            if isinstance(p, PhongVIP):
                phong_data["phi_don_dep"] = p.phi_don_dep
                phong_data["phi_minibar"] = p.phi_minibar
            data["phongs"].append(phong_data)

    for phieu in danh_sach_phieu:
        data["phieus"].append({
            "ma_khach": phieu.khach_hang.ma_khach,
            "ten": phieu.khach_hang.ten,
            "so_cccd": phieu.khach_hang.so_cccd,
            "ma_phong": phieu.phong.ma_phong,
            "so_ngay": phieu.so_ngay,
            "tong_tien": phieu.tong_tien
        })

    with open("khachsan_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_data():
    try:
        with open("khachsan_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"phongs": [], "phieus": []}


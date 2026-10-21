ma_may = input("Nhap ma may: ")
cong_suat_w = input("Nhap cong suat W: ")
so_phut = input("Nhap so phut su dung: ")
don_gia_kwh = input("Nhap donn gia dien/kWh: ")

print("Kieu ma may:", type(ma_may))
print("Kieu cong suat:", type(cong_suat_w))
print("Kieu so phut:", type(so_phut))
print("Kieu don gia:", type(don_gia_kwh))

cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("May:", ma_may)
print("dien nang:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phi:", chi_phi, type(chi_phi))
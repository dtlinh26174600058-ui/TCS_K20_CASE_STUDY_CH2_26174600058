#ma_may = input("Nhap ma may: ")
#cong_suat_w = input("Nhap cong suat W: ")
#so_phut = int(input("Nhap so phut: "))
#dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
#rint(f"May: {ma_may}")
#rint(f"Dien nang: {dien_nang:.3f} kWh")
#Loi 1: tep Cau07_chan_doan_loi.py 
#loi dong 6
#loai loi: type error
#Thong bao loi: Typeerror: unspported operand type(s) for /: 'str' and 'int'
#nguyen nhan: do thieu dau ) cuoi lenh print 
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = float(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} Kwh")
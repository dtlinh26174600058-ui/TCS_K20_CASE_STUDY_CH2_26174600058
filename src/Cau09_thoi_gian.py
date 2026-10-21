from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
#datetime: Kieu thoi diem(ngay gio cu the), tru duoc cho nhau
#str: Chuoi chu, o day la thoi diem da dinh dang bang strftime de hien thi khong tinh toan thoi gian duoc
#timedelta: Kieu khoang thoi gian, la ket qua cua phep tru hai datetime (o day la 1 gio 50 phut)
# computer_inventory = {
#     "HP": 20,
#     "DELL": 50,
#     "MACBOOK": 12,
#     "ASUS": 30
# }

# bang_gia = {
#     "HP": 600,
#     "DELL": 650,
#     "MACBOOK": 1200,
#     "ASUS": 400
# }

# tong_gia_tri_theo_hang = {}

# for hang, so_luong in computer_inventory.items():
#     gia = bang_gia[hang]
#     tong_gia_tri = so_luong * gia
#     tong_gia_tri_theo_hang[hang] = tong_gia_tri

# print("Tổng giá trị của từng hãng trong kho:")
# for hang, tong_gia_tri in tong_gia_tri_theo_hang.items():
#     print(f"{hang}: {tong_gia_tri}")
computer_inventory = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

bang_gia = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

tong_gia_tri_kho = 0

for hang, so_luong in computer_inventory.items():
    gia = bang_gia[hang]
    tong_gia_tri_kho += so_luong * gia

print("Tổng giá trị của toàn bộ máy trong kho:", tong_gia_tri_kho)

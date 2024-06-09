computer_inventory = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}
brand = input("Nhập tên hãng máy tính: ")
count = int(input("Nhập số lượng máy: "))
if brand in computer_inventory:
    so_luong_may_asus = count
    gia_asus = computer_inventory[brand]
    tong_gia_tri_don_hang = so_luong_may_asus * gia_asus
    print("Tổng giá trị của đơn hàng đặt mua 5 máy ASUS là:", tong_gia_tri_don_hang)
else:
    print("Không có thông tin về hãng máy tính này trong kho.")

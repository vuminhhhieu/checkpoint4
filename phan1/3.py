computer_inventory = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
brand = input("Nhập tên hãng máy tính: ")
if brand in computer_inventory:
    print("Số lượng", brand, "có trong kho là:", computer_inventory[brand])
else:
    print("Không có thông tin về hãng máy tính này trong kho.")

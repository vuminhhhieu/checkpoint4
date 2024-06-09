computer_inventory = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}
brand = input("Nhập tên hãng máy tính: ")
if brand in computer_inventory:
    print("Giá tiền của", brand, "là:", computer_inventory[brand])
else:
    print("Không có thông tin về hãng máy tính này trong kho.")
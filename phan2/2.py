computer_inventory = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
brand = input("Nhập tên hãng máy tính: ")
count = int(input("Nhập số lượng máy: "))
computer_inventory[brand] = count
print(computer_inventory)
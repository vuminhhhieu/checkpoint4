skills = [
    {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
]

print("Các skill của nhân vật:")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill['Name']} (Damage: {skill['Damage']}, Minimum level: {skill['Minimum level']})")


choice = int(input("Chọn skill (nhập số tương ứng): "))

player_level = 3
if choice < 1 or choice > len(skills):
    print("Lựa chọn không hợp lệ!")
else:
    selected_skill = skills[choice - 1]
    min_level = selected_skill["Minimum level"]
    if player_level < min_level:
        print("Level của nhân vật không đủ để sử dụng skill này!")
    else:
        damage = selected_skill["Damage"]
        print(f"Nhân vật sử dụng skill '{selected_skill['Name']}' và gây ra {damage} sát thương!")

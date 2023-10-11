my_list = [1, 2, 3.5, "four", 5, 6, 7, 8, 9, 10, 11, 12, "thirteen"]
my_list="(99)999-99-99"

indices_to_check = [3, 5, 6, 10, 11, 12]
indices_to_check = [1,2,4,5,6,8,9,11,12]

for index in indices_to_check:
    if 0 <= index < len(my_list) and isinstance(my_list[index], (int, float)):
        print(f"Element at index {index} is a number: {my_list[index]}")
    else:
        print(f"Element at index {index} is not a number or is out of bounds.")

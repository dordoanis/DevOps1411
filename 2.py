# my_number = "4"
# result = float(my_number) - 2
# print(result)
# print("your result is " + str(result))
# print(f"your result is {result}")
# my_str = "hello and welcome to devops experts"
# my_list = [1, 2, 3, 4, 5, 6]
# print(f"your result is {my_list[2:0 - 1]}")
# print(my_list[0:5:2])
# print(my_list[0::3])
# print(my_list[::3])
# print(my_str[::2])

my_dict = {"name": "Dor", "lname": "Doanis", "age": 27, "ID": 315707596}
print(my_dict)
# key_to_print =input(f"enter key: ")
key_to_print = input(f"enter key {list(my_dict.keys())}: ")
print("you chose to print: " + str(my_dict[key_to_print]))

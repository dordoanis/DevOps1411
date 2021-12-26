
# import requests
# try:
#     response = requests.get("https://blablabla.com")
# except requests.exceptions.ConnectionError:
#     print("Unable to connect to host ")

# try:
#     a = int(input("enter first num: "))
#     b = int(input("enter first num: "))
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("could not divide by Zero")
# except BaseException as e:
#     print("somthing went worng " + str(e.args))


def get_user_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("Age can not be negativ")
    return age

age = -1
while age < 0:

    try:
        get_user_age()
    except ValueError as e:
        print(e.args[0])

print(f"your age: {age}")

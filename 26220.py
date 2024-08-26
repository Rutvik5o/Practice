user_dict = {}

num = int(input("enter how many entries you want to?->"))

for i in range(num):

    key = input("Enter key")

    value = input("Enter value")

    user_dict[key] = value


print(user_dict)

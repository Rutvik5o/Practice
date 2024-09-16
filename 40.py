user_dict = {}

num = int(input("Enter how many entires you want->"))

for i in range(num):

    key = input("Enter Key->")

    value = input("Enter value->")

    user_dict[key] = value


print("Dictionary=>",user_dict)
# def show_username():
#     Result = "Hello username"
#     return Result

# print(show_username())



# def area_rect(l, b):
#     answer = l * b
#     return answer

# l = 10
# b = 5
# print(area_rect(5, 10))
# print(area_rect(20, 8))


# def greeting(username):
#     grt = f"Hello {username}"
#     return grt


# username = input("Enter your username: ")
# print(greeting(username))


# def more_numbers(*args):
#     return sum(args)

# print(more_numbers(5, 7))
# print(more_numbers(15, 7, 20))


# def check_name(name):
#         return name

# def greet_user(name_from_first):
#     greeting = f"Welcome {name_from_first}"
#     return greeting

# name = input("Enter a name: ")
# name_from_first = check_name(name)
# print(greet_user(name_from_first))

# type hint

def sub_two(num1 :int, num2 :int) -> int:
    """
    This function is to subtracting two numbers
    """
    return num1 - num2
print(sub_two(10, 4))

greeting = lambda username: f"Welcome{username}"
result = lambda number: number + 1
print(result(45))
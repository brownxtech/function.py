# # print()
# # print(889)

# #def greeting(name):
#     #result = f"Welcome {name} "
#     #return result

# #your_name = "shegun"
# #print(greeting(your_name))

# # def addTwoNumbers():
# # def addtwonumbers():
# # def  AddTwoNumbers():
# def add_two_numbers(first, second):
#     return  first + second

# first_num = input("Enter first number: ")
# second_num = input("Enter second number: ")
# print(add_two_numbers(first_num, second_num ))
# print(add_two_numbers(first_num, second_num ))


def show_workings():
    message = "weldone"
    name = "shegun"
    return message, name

# our_funct = show_workings()
first, second = show_workings()
print(second)



students={
    "shegun":70,
    "mic":20,
    "john":10
}
# print(dir(students))
# print(student.items())
for student in students.items():
    print(student)

def add(num1, num2):
    return sum(num1, num2)

def add(*args):
    return sum(args)

print(add(30,20))
print(add(30,20,40 ))
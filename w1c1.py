print("Hello world")
a = 18
print(a)

b = 9
print(b)

name = "111"
print(name)

name = "2233"
print(name)

first_name = "x"
print(first_name)

age = 28

if age > 18 and age < 75:
    print("Adult")
elif age > 75:
    print("Old")
else:
    print("Get your parents kiddo!!!")
    
print(not(10 > 5))
print(10 > 5)

numbers = [1, 3, 5, 11, 10]
for i in numbers:
    print(i)
    
numbers = [1, 3, 5]
print(numbers[1])
numbers[0] = 30
print(numbers)

my_dict = {"name": "111", "age": 25, "height": 170}
print(my_dict["name"])

staff = [{"name": "111", "age": 25, "height": 170},
          {"name": "222", "age": 28, "height": 160}]
print(staff[0]["name"])
print(staff[1]["height"])

def add_one(num):
    return num + 1
print(add_one(10))
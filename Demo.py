print("Hello, world!")
age = 18
if age > 18 and age < 65:
    print("adult")
elif age > 65:
    print("old")
else:
    print("kids")
PI = 3.14
MIN_SIZE = 100
print(PI+MIN_SIZE)
my_string = "Hello, world!"
another_string = 'python is fun'
multiline_string = """This is a
multiple-line string."""
greeting = "How are you"
name = "Emma"
message = greeting + "," + name + "."
print(message)
exciting = "omg"
too_much_excitement = exciting * 5
print(too_much_excitement)
print(greeting[4])
print(greeting[4:7])
message = "I miss you so much"
message_1 = message.upper()
message_2 = message.lower()
message_3 = message.strip()
print(message_1+message_2+message_3)
message = "     I LOVE YOU     "
re_message = message.strip()
print(re_message)
print(message)
sentence = "I don't like pineapples."
index = sentence.find("apples")
print(index)
new_sentence = sentence.replace("pineapples", "pears")
print(new_sentence)
data = "1, 3, 5, 7"
numbers = data.split(",")
print(numbers)
not_sentence = ".".join(numbers)
print(not_sentence)
name = "Emma"
height = "169cm"
message = "Hello, {}. Your height is {}.".format(name, height)
print(message)
message_2 = f"Hello, {name}. Your height is {height}."
message = f"Dear {name}, \nHope this message finds you well."
print(message)
message = "Hello\"World\""
print(message)
number = int(3.1415926)
print(number)
import random
random_integer = random.randint(45,90)
print(random_integer)
print("Hello, world", end = ".")
print(" I wanna say more.")
string_number = "10"
convert_to_float = float(string_number)
print(f"string '{string_number}' is now converted to float {convert_to_float}.")
print(type(convert_to_float))
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
    print("Fruit is delicious!")
nest_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nest_list[0])
print(nest_list[0][1], nest_list[2])
message = f"My favorite fruit is {fruits[1]}."
print(message)
length = len(fruits)
print(length)
fruits.append("watermenlon")
fruits.insert(1,"cherry")
others = ["grapes", "pineapple"]
fruits.extend(others)
print(fruits)
removed_fruit = fruits.pop()
print(fruits)
sorted_fruits = sorted(fruits, reverse = True)
# reverse = True means 字母的逆序排列
numbers = [4, 5, 3, 1]
numbers_reverse = sorted(numbers, reverse = True)
# outcome = [5, 4, 3, 1]
print(numbers_reverse)
numbers.reverse()
print(numbers)
# outcome = [1, 3, 4, 5]
#sort(xx, reverse = True)和xx.reverse()的用法是不一样的
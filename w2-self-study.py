# the use of range()
for t in range(7):
    print(t)

# range(start,stop)
for i in range(3,6):
    print(i)

#range(start,stop,step)
for x in range(10,19,3):
    print(x)

#create lists from range
numbers=list(range(2,7))
print(numbers)

#sum(), min(), max()
numbers=[2,6,10,3]
total = sum(numbers)
print(total)
small_number = min(numbers)
large_number = max(numbers)
print(sum(numbers)+small_number)

#new_list = [expression for item in iterable] + if sentence
numbers=[1,2,3,4,5,6]
new_list = [t**3 for t in numbers]
print(new_list)
new_list_1 = [s**2 for s in numbers if s%2==0] # % stands for 余数
print(new_list_1)
new_list_2 = ["odd" if y%2!=0 else "even" for y in numbers]
print(new_list_2)
# same for 3D to 2D list
three_dimensional_list = [[1,2],[3,4],[5,6]]
two_dimensional_list = [item for sublist in three_dimensional_list for item in sublist]
# sliced_list=original_list[start:stop:step]
numbers = [2,3,4,5,6,7,8]
sliced_list=numbers[3:7:2]
print(sliced_list)
# outcome is [5,7; stop的是索引（也就是顺序，从0开始）而不是列表中的数字
# 负着来没有从-1开始而不是0

# Looping through a slice
numbers = [5,6,7,8,9,10]
for t in numbers[1:4]:
  print(t)

# to copy the list: copy(), list[:], list()
# copy() and deepcopy()
  
# 任何修改、添加或删除tuple中的元素都会error
this_tuple = (2,3,4)
this_tuple[2] = 7
# outcome is error
# Updating Tuples through Reassignment
origional_tuple = (1,2,3)
new_tuple = (origional_tuple[0],4,origional_tuple[2])
origional_tuple = new_tuple

# in-class exercise for Lecture 03 List

# 1. Fill in the missing code to produce the output: ['honda', 'yamaha', 'suzuki', 'kawasaki']
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
motorcycles.append('kawasaki')
print(motorcycles)


# 2. Please double each element in the list 
my_list = [1, [4, 6, 12], 7, 8]
my_list[0] = my_list[0] * 2
my_list[1] = [x * 2 for x in my_list[1]] 
my_list[2] = my_list[2] * 2
my_list[3] = my_list[3] * 2       
print(my_list)

# 3. Fill in the code to produce the following output:  [3, 6, 99, 45, 29, 34] 
#    You can insert multiple lines of code, obtain target_list based on list1 and list2
list1 = [3,6,99,12]
list2 = [64,45,29,34]

target_list = list1 + list2
target_list.remove(12)
target_list.remove(64)
#target_list = [] # comment out this line 
print(target_list)

# Try it yourself exercise
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit

# (1) Store the locations in a list
seeing_the_world = ['Spain', 'Japan', 'Greece', 'Australia', 'Italy']

# (2) Print your list in its original order
print("Here is the original list:")
print(seeing_the_world)

# (3) Print your list in alphabetical order without modifying the actual list
print("\nHere is the list in alphabetical order:")
print(sorted(seeing_the_world))

# (4) Show that your list is still in its original order by printing it
print("\nHere is the original list again:")
print(seeing_the_world)

# (5) Change the order of your list in reverse order and print it
print("\nHere is the list in reverse order:")
seeing_the_world.reverse()
print(seeing_the_world)

# (6) Change your list so it’s stored in reverse-alphabetical order, and print it 
print("\nHere is the list in reverse alphabetical order:")
seeing_the_world.sort(reverse=True)
print(seeing_the_world)

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
print("4-3. Counting to Twenty:")
for value in range(1, 21):
    print(value)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list. 
print("4-7. Multiples of 3:")
for value in range(3, 31, 3):
    print(value)

'''
4-8. Cubes: A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. Make a list of the 
first 10 cubes (that is, the cube of each integer from 1 through 10), and 
use a for loop to print out the value of each cube. 
'''
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
    print(cube)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
print("4-9. Cube Comprehension:")
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# in-class code
import copy

list1 = [1, 2, 3, 4, ["a", "b"]] 
list2 = list1 
list3 = list1[:]
list4 = list1.copy()
list5 = copy.copy(list1) 
list6 = copy.deepcopy(list1) 

# adds 5 to the end of list2 (and list1 too, since they are the same object)
list2.append(5) 

# adds "c" to the inner list ['a', 'b'] — affects list1 and list3 because they share that inner list     
list3[4].append("c") 

# changes only list4’s first element to 100 (does NOT affect list1)
list4[0] = 100   

# replaces the last item in the shared inner list with "w" — affects list1,2,3,4,5    
list5[4][-1] = "w"   

# adds "c" to the inner list in list6 only, because deepcopy makes it independent
list6[-1].append("c")

# discuss the answers before running the following code
print(f"list1: {list1}") # list1: [1, 2, 3, 4, ['a', 'b', 'w'], 5]
print(f"list2: {list2}") # list2: [1, 2, 3, 4, ['a', 'b', 'w'], 5]
print(f"list3: {list3}") # list3: [1, 2, 3, 4, ['a', 'b', 'w']]
print(f"list4: {list4}") # list4: [100, 2, 3, 4, ['a', 'b', 'w']]
print(f"list5: {list5}") # list5: [1, 2, 3, 4, ['a', 'b', 'w']]
print(f"list6: {list6}") # list6: [1, 2, 3, 4, ['a', 'b', 'c']]

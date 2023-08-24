## General Info

Python has 4 built-in data types: lists, tuples, sets, and dictionaries, all with different qualities and usage.
## Sorting

```python
nums = [3, 4, 6, 5, 2, 1]
nums.sort() # [1, 2, 3, 4, 5, 6]

# USEFUL !
# can sort using a lambda key function

intervals = [[1, 3], [2, 4], [4, 6]]
intervals.sort(key = lambda i : i[0])

cities = [
	{
		"name": "New York City",
		"country": "United States",
		"population": 20.14,
		"area": 1223.59
	},
	{
		"name": "Tokyo",
		"country": "Japan",
		"population": 37.47,
		"area": 2194.07,
	},
	{
		"name": "Los Angeles",
		"country": "United States",
		"population": 13.2,
		"area": 1299.01,
	},
]

# sorting by population
cities = cities.sort(key = lambda city: city["population"])

# descending order using the '-' sign
cities = cities.sort(key = lambda city: -city["population"])

# lambda is still a fn, so you we can do some calculation
cities = sorted(cities, key=lambda city: (city['population'] / city['area']))
```

## Turn strings into integers

```python
c = '2'
num = int(c) # becomes 2 of integer type
```
## Iterables

An iterable is a Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.

Some examples include:
- Lists
- Tuples
- Strings
## Shallow vs deep copy

Performed using the copy library:

```python
import copy

a = [1, 2, 3, 4]
b = "hello"

a1 = copy.copy(a)
b1 = copy.copy(b)

a2 = copy.deepcopy(a)
b2 = copy.deepcopy(b)
```

Note: normal assignment operations will simply *point* the new variable towards the existing object.

The difference between shallow and deep copying is only relevant for *compound objects* (objects that contain other objects, like lists or class instances, I think objects with 'children' elements):
- A shallow copy constructs a new compound object and then inserts *references* into it to the objects (contained within it?) found in the original
- A deep copy constructs a new compound object and then *recursively* inserts copies into it of the objects found in the original 

## Lists

Basically a dynamic array

```python
nums = [1, 2, 3] # declaring a list

list(nums) # creates a shallow copy of the list

nums.index(1) # returns index of specified item
nums.append(1) # appends item to end of list
nums.insert(0, 9) # inserts 9 at the first index
nums.remove(9) # removes all instances of 9
nums.copy() # returns a shallow copy of the list, i.e. when you modify this copy, the original is also modified – if you don't want that behaviour, use copy.deepcopy(nums)
nums.count(9) # returns no. of occurences of 9 in nums
nums.extend([4, 5, 6]) # adds all items to end of nums
nums.pop() # pops last element
nums.reverse() # reverses list order
nums.sort() # note: does NOT return sorted list, sorts in-place using default Tim Sort, a combo of merge + insertion sort
```

```python
chars = ['a', 'b', 'c']

chars[start:stop] # items from start through stop - 1
chars[start:] # items from start to end
chars[:stop] # items from beginning through stop - 1
chars[:] # a copy of the whole array

# note: the :stop value is the *first* value NOT in the slice. that's why it's stop - 1. perfect for using len(chars).
# print(chars[0:len(chars)]) prints ['a', 'b', 'c']

chars[start:stop:step] # start through not past stop, by step

# start and end can be negative, i.e. counts from end of array instead of beginning
chars[-1] # last item, ['c']
chars[-2:] # last two items ['b', 'c']
chars[:-2] # everything except last two item, ['a']

# step can also be negative
chars[::-1] # reverses all items in the array
chars[1::-1] # first two items, reversed
chars[:-3:-1] # last two items, reversed
chars[-3::-1] # everything except last two items, reversed
```

![[python_lists_time_complexity.png]]
## Dictionary

```python
dict = {} # creates empty dictionary
dict2 = dict() # also creates empty dictionary

words = {
	'a' : 1,
	'b' : 2,
	'c' : 3
}

dict.keys() # returns list of keys
dict.values() # returns values of keys
dict.get('a') # returns value for specified key, 1
dict.items() # returns [('a', 1), ('b', 2), ('c', 3)], i.e. a list of dictionary's *tuple* pairs
dict.copy() # returns a copy of the dictionary
dict.pop('a') # pops key-value pair with that key
dict.popitem() # removes most recently added pair
dict.setDefault(key, default_val) # if key exists, default_val has no effect; else, it becomes key's default val

# USEFUL !
dict.update({ key: value }) # inserts pair in dict if not present, else value is overriden

# ALSO USEFUL !
if key in dict: 
	dict[key] += 1 
else: 
	dict[key] = 1
```
## Counter

```python
from collections import Counter
# or could use collections.Counter()

list = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1]

counterList = Counter(list) # gives { 1: 3, 2: 2, 3: 2, 4: 2, 5: 1}
counterList.keys() # returns [1, 2, 3, 4, 5]
counterList.most_common(x) # returns the x most common element, so if x = 1, it would return [(1: 3)]
counterList.update([1, 2, 3]) # counterList becomes {1: 1, 2: 1, 3: 1}
counterList[1] # returns frequency of specified key

s = "hello world";
for count in collections.Counter(s).values():
	print(count); # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

## Deque

A double-ended queue, represented internally as a doubly linked list. Useful as a stack (LIFO) or queue (FIFO).

Stack:
- Append to the left / front / top
- Pop from the left / front / top
- Use append and pop, or appendleft and popleft for both operations

Queue:
- Append to the right / end / bottom
- Pop from the left / front / top
- Use append and popleft

```python

from collections import deque

queue = deque([1, 2, 3])

queue.append(4) # append to right / end, [1, 2, 3, 4]
queue.pop() # pop from right / end NOT left / front, [1, 2, 3]

queue.appendleft(0) # append to left / front, [0, 1, 2, 3]
queue.popleft() # pop from left / front, [1, 2, 3]

queue.index(elem, begin_index, end_index) # returns index of elem between begin_index and end_index if specified
queue.insert(index, elem) # inserts elem at index
queue.remove(elem) # removes specified elem 
queue.count(elem) # returns no. of occurences of elem
queue.reverse() # reverses order of elems
```

## Heapq

Most commonly used to implement a priority queue.

`heapq.heapify()` is an *in-place* heapify and can be done in O(n).
`heapq.heappush()` and `heapq.heappop` are O(logn).

```python
import heapq

def findKthLargest(self, nums, k):
	heap = heapq.heapify(nums) # heapify array of numbers

	for _ in range(len(nums) - k): # pop until we get Kth largest element
		heapq.heappop(heap)
		
	return heappq.heappop(heap) # do one last pop to return Kth largest element
```

## Set



## Destructuring in loops

```python
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for row, col in directions:
	print(row, col)

# 0, 1, 0, -1, 1, 0, -1, 0

for direction in directions:
	print(direction[0], direction[1])

# prints same thing
```

## Declaring a class in Python

Syntax:

```python
class ClassName: 
	# fields, constructor 
	public_member #can be accessed from outside the class 
	
	# cannot be accessed from outside the class, shown with two underscores
	__private_member
```

```python
class Node:

	# the constructor
	def __init__(self, val, next):
		self.val = val
		self.next = next

	# other methods
	def print_val():
		print(self.val)
```
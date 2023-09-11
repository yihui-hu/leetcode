## Breadth-First-Search (BFS)

Process entails traversing all nodes of a graph without re-visiting already visited ones.

Most common data structure to implement BFS algorithm: a queue that you add nodes to and their neighbouring nodes, along with a visited hash map of sorts.

Pseudocode:
1. Create queue Q
2. Mark V as visited and put into Q
3. While Q is not empty:
	1. Pop from Q
	2. Add unvisited neighbours from popped V

```python
# suppose you are given a graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# initialize stacks to help with BFS
visited = []
queue = []

# define helper function for BFS
def bfs(visited, graph, node):
	visited.append(node) # mark node as visited
	queue.append(node)

	while queue: # while queue is not empty
		m = queue.pop(0) # pop vertex off queue
		for neighbor in graph[m]: # get neighbors from graph
			if neighbor not in visited: # if neighbor not already visited
				# process here?
				visited.append(neighbor)
				queue.append(neighbor)

bfs(visited, graph, '5')
```

## Depth-First-Search (DFS)

Instead of using stacks, we use recursion in order to traverse deeper and deeper into the graph or tree, processing each one and then escaping to outer functions, checking if we've visited them already as well

```python
# this is graph implementation

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # set to keep track of visited nodes

def dfs(visited, graph, node):
	if node not in visited: # only process node if not already in visited
		visited.add(node)
		for neighbor in graph[node]: # for each neighbor of node, traverse
			dfs(visited, graph, neighbor)

dfs(visited, graph, '5')
```
## Level Order Traversal (BFS)

From left to right, level order
## In Order Traversal

1. Traverse the left subtree, i.e., call Inorder(left->subtree)
2. Visit the root.
3. Traverse the right subtree, i.e., call Inorder(right->subtree)
## Trie

A trie (pronounced `"try"`) is special kind of tree – it is a *prefix* tree used to efficiently store and retrieve strings. It's commonly used for things like autocomplete and spellcheckers.

## Dijkstra's algorithm

## Floyd Warshall's algorithm

## Fibonacci heap

## Binary heap

## Min/max heap

## Floyd's cycle finding algorithm (fast and slow pointers)

Establish a `slow` and `fast` pointer where `fast` moves 2 steps and `slow` moves 1 step:

```python
while fast and fast.next:
	fast = fast.next.next;
	slow = slow.next;
```

Useful for the following problems:
- Finding middle of linked list
	- Use `fast` and `slow` pointers: `slow` will be in middle of list (2nd middle if if even number) once `fast` reaches the end
- Determining if linked list is palindrome
	- Find middle pointer using `slow`, reverse second half of linked list, then use `head` and `fast` to 'walk' forward and backward and determine if LL is palindromic
- Detecting a cycle
	- Eventually the `slow` and `fast` pointer will meet 

```python
function detectCycle(head) {  
	fast = slow = head  
	
	while fast and fast.next {  
		fast = fast.next.next  
		slow = slow.next  
		if fast === slow return true  
	}  
	
	return false  
}
```

## Getting digits from number

```python
n = 100
output = 0

while n:
	digit = n % 10
	output += digit
	n = n // 10 # move to the next place
```
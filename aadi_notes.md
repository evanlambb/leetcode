# Dijkstra's
- Gets the minimum distance for each node from a source
- Use a priority q (min heap) and visited set
- The priority q should be sorted according to the distance for that node, and should be initialized to contain just the source at first
- Iteratively add the nearest nodes for each node in the q to the heap, and then visit the minimum node in the heap each time
- Visited nodes should be added to the set and not visited again as the minimum distance calculated is guaranteed
``` Python
# Weighted graph
graph = defaultdict(list)
for edge in edges:
	graph[edge[0]].append((edge[1], edge[2])) # Destination and weight

visited = set()
q = [(0, source)]
heapq.heapify(q)
distances = {}

# Initialize distances to be infinity except for source
for i in range(n):
	distances[i] = float("inf")
distances[source] = 0

while q:
	distance, node = heapq.heappop(q)
	if node in visited:
		continue
	visited.add(node)
	for edge in graph[node]:
		to, weight = edge
		if weight + distance < distances[to]:
			distances[to] = weight+distance
			heapq.heappush(q, (weight + distance, to))
return distances
	
```

# Kosaraju's
- To determine if a directed (sub)graph is strongly connected, run DFS on the original graph and verify that all vertices are visited, and verify that running DFS on the transposed graph also allows the same vertices to be visited
# Eulerian Path or Circuit
- An Eulerian Cycle is a cycle that visits every edge exactly once and ends on the same node than it started on
- An Eulerian Path is a path that visits every edge exactly once, and may end on a different node than it started on
- An Eulerian Cycle requires:
	- All vertices with non-zero degree are part of a single (strongly for directed graph) connected component
	- Every vertex in the graph has an even degree (in degree = out degree for directed graph)
- An Eulerian Path requires:
	- All vertices with non-zero degree are part of a single (strongly for directed graph) connected component
	- Either exactly 2 or 0 vertices in the graph have odd degree (0 means Eulerian Cycle)



# Hierholzer's
- Finds a Eulerian Cycle given a directed graph that contains one
- Starts at an arbitrary vertex $v$ and follows a trail until either getting stuck at $v$ or visiting every edge
	- Can only get stuck at $v$ since in degree matches out degree of every vertex
- As long as there exists a vertex $u$ that belongs to the current tour, but that has adjacent edges not part of the tour, start another trail from u, following unused edges, until returning to u, and join the tour formed in this way to the previous tour
- Practically, this involves exploring a path and adding nodes the the final result when backtracking after being stuck
	- Once all nodes are backtracked (no edges remain), the final result must be reversed to get the Eulerian Circuit in correct order
	- Accomplished using a stack
``` Python
graph = defaultdict(list)
for edge in edges:
	graph[edge[0]].append(edge[1])

# Start from vertex 0 assuming it is in the connected component
stack = [0]
result = []
while stack:
	node = stack[-1]
	if node in graph and len(graph[node]) > 0:
		stack.append(graph[node].pop())
	else:
		result.append(stack.pop())
return result[::-1]
```
# Prim's
- Used to find the minimum spanning tree in a graph
- Involves keeping 2 sets, one for vertices in the MST, and one for not in the MST, and using a priority q to pick the minimum weight edge that connects a vertex from the MST to a vertex thats not in the MST
- Once the non-MST set is empty, the MST has been built
``` Python
graph = defaultdict(list)
for edge in edges:
	graph[edge[0]].append((graph[2], graph[1])) # Add other way around as well for undirected

# Prims

# Start at arbitrary node, in this case 0
mst = {0}
not_mst = set(range(1, n))
q = [] # Heapq for edges
cost = 0
for edge in graph[0]:
	heapq.heappush(q, edge)

while len(not_mst) != 0:
	edge = heapq.heappop(q)
	if edge[1] in mst:
		continue
	cost += edge[0]
	mst.add(edge[1])
	not_mst.remove(edge[1])
	for e in graph[edge[1]]:
		heapq.heappush(q, e)
return cost
```

# Union Find
- A data structure used to find and create the union of disjoint sets
- A representative root parent is stored for each group
	- Unionizing two sets involves switching the pointer of the smaller set's root parent to point to the root of the larger set
	- Finding involves returning the representative parent by traversing the nodes parents until reaching the root, flattening the tree in the process to reduce future lookup time
``` Python
par = list(range(n))
rank = [1] * n

def find(n):
	res = n

	# The root has itself as its parent
	while res != par[res]:
		par[res] = par[par[res]] # Set parent to grandparent to flatten tree
		res = par[res] # Move up tree

	return res

def union(n1, n2):
	p1, p2 = find(n1), find(n2)

	if p1 == p2:
		return 0 # Already part of same set

	# Merge smaller set into larger set
	if rank[p1] > rank[p2]:
		par[p2] = p1
		rank[p1] += rank[p2]
	else:
		par[p1] = p2
		rank[p2] += rank[p1]
	
	return 1 # Successfully merged sets
	
```

# Kahn's
- Topologically sorts a graph by first getting the in-degree of every node, and adding all nodes with in-degree 0 to a queue
- While the queue is not empty:
	- Remove a node from the front of the queue, add it to the sorted list, and decrement the in-degree of all nodes that it has an outgoing edge to
	- If the in-degree becomes 0 then add it to the end of the queue
- If the queue becomes empty and there are still nodes in the graph, the graph contains a cycle and can't be sorted topologically
# Floyd's 
- Detects the start of a cycle in a linked list
- Uses 2 pointers to traverse the linked list, a fast pointer and a slow pointer
	- The fast pointer moves up 2 nodes each time and a slow pointer moves 1
	- If the pointers ever equal each other there is a cycle
- The distance of where the 2 pointers meet to the start of the cycle and the start of the linked list to the start of the cycle is equal
- Move each slow pointer until they meet, and that is the start of the cycle 
# Floyd-Warshall
- Involves considering every possible intermediate node between two nodes to find the shortest path between two nodes, relying on the fact that any path of nodes is consisting of sub paths between two nodes with intermediate nodes
```Python
for k in range(V):
	for i in range(V):
		for j in range(V):
			if distances[i][k] != float("inf") and distances[k][j] != float("inf"):
				distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
```

# Kruskal's
- Finds the MST by sorting the edges in ascending cost, and repeatedly adding the edges with minimal cost that connects to disjoint sets
- Determines if a set is disjoint using a Union-Find data structure, and stops when V-1 edges have been added
``` Python
edges.sort()
E = len(edges)
V = len(vertices)
dsu = DSU(V)
connections = 0
cost = 0
for edge in edges:
	if dsu.find(edge[0]) != dsu.find(edge[1]):
		cost += edge[2]
		connections += 1
		dsu.union(edge[0], edge[1])
		if connections == V-1:
			break
return cost
```
# Bellman Ford's
- Finds the minimum distance from a source, but can handle negative edge weights unlike Dijkstra's
- Performs V-1 relaxations, where each relaxation recalculates the minimum distance for each edge, and then a final relaxation to detect a negative cycle, meaning a possible minimum distance of negative infinity
``` Python
distances = [float("-inf")] * V
distances[src] = 0
for i in range(V):
	for edge in edges:
		if distances[edge[0]] + edge[2] < distances[edge[1]]:
			if i == V-1:
				return -1 # Negative cycle as no distances should be updated on the V-1th iteration

			distances[edge[1]] = distances[edge[0]] + edge[2]
return distances
```
# Kadane's
- To find the maximum sum subarray, simply traverse the array, and when the current sum becomes negative move the left pointer to the current index + 1 and reset the current sum to 0

# 0-1 BFS
- Identical to Dijkstra's except instead of a priority queue, a double ended queue can be used, and when an edge of weight 0 is encounter, append it to the left, when an edge of weight 1 is encounter, append it to the right
# Possible
	- Dinic
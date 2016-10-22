Shortest Paths in a Network
Author: Sumant Sanjay Tapas
Email ID: stapas@uncc.edu

Program and Data Structure design:

The project is implemented using python 3.4. It uses object oriented programming concepts in python.
There are 3 classes in the program:
	1. Vertex: vertex class holds all the information of a vertex. 
			Member variables:	
				a. Name - type: String
				b. Adjacency list - type: list 
				c. Distance - type: int
				d. Previous Vertex- type: Vertex
				e. Status - type: int
			Member Functions:
				reset() - This function set the Distance to infinity and the Previous Vertex to nil.
		The constructor needs 'name' as a parameter to assign it.
	2. Edge: Edge class holds information of an edge. 
			Member variables:
				a. Weight - type: int
				b. Vertex - Destination vertex, type: Vertex 
				c. Status - type: int
			Objects of Edge class reside in the adjacency list of the vertex.
			       5
			(A) -------> (B)
			
			For example, if vertex A has an edge to vertex B with weight 5. Then an edge object with weight = 5, Vertex = B and status = 1 would be added to A's adjacency list.
	3. Graph: Graph class holds information regarding a graph.
			Member variables:
				a. vertexMap - Hashtable to hold the vertex objects. Type: dictionary
			Member Functions:
				All the functionality required by the project is performed using the member functions of this class. Few of the important functions are:
				shortestPath(), reachable(), printGraph().
				
The program implements an OSPF protocol using Dijkstra's algorithm to find the shortest path between vertices. The priority queue used in Dijkstra's algorithm is implemented using a list of tuples as a binary Min Heap. Each tuple contains (distance, Vertex) pair. The priority is calculated using the distance element in the tuple. Functions minHeapify(), extractMin(), buildMiHeap(), decreasePriority() helps to build and maintain the priority queue. Note that these functions are not part of any class, they are independent functions. The Min heap takes O(logV) time to complete all operations except buildMiHeap() which takes O(V) time. 

The graph class function reachable is implemented using a DFS like algorithm. A loop traverses through all active vertices. For each vertex, it's adjacency list is traversed and each visited vertex is added to list of visited vertices. Now for each vertex in the adjacency list a recursive function is called until all vertices are visited. In this way, the function goes deep just like DFS for each vertex. Hence the running time of the algorithm should be V times the time complexity of DFS which is O(V*(V+E)), where V is the set of vertices and E is the set of edges.   

The program will fail to calculate shortest path if the weights associated with the edge is negative.
				
Break down of files:

The OSPF_Dijkstras.py is the file for the project. It requires 1 command line parameter: text file having the initial condition of the graph.  

How to Run the program:

The programs are implemented using python 3.4. Following are the ways to run the programs on different OSs.  

Windows:
1. Open Powershell
2. set the environment variable to - [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python34") where 
   'C:\Python34' is the path is the path to your python 3.4 interpreter.
3. Type in the following command in the directory of the file OSPF_Dijkstras.py : python OSPF_Dijkstras.py network.txt

Linux:
1. Open Terminal
2. Check for the python version by using the following code:
   $ python --version
   It should be 3.4   
3. Type in the following command in the directory of the file OSPF_Dijkstras.py: python3 OSPF_Dijkstras.py network.txt 

   
Where, network.txt is the input file containing the initial graph

Also, the program expects the network.txt file in the same directory as the OSPF_Dijkstras.py file

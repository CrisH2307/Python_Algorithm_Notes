# Classification of Data Structure
## Linear Data Structures
Linear data structures are arrangements of data elements where each element has a unique predecessor and successor, forming a sequential order.
1. Array: A linear collection of elements with indexed access for efficient retrieval.
2. Linked List: Elements connected by pointers, allowing dynamic allocation and efficient insertions/deletions.
3. Stack: Follows the Last-In-First-Out (LIFO) principle with top-based element manipulation.
4. Queue: Adheres to the First-In-First-Out (FIFO) concept, used for ordered processing.
5. Deque: Supports insertion and removal at both ends, offering enhanced flexibility.

#### The Need for Linear Data Structures
+ Ordered Storage: Linear data structures maintain a sequential order, which is essential for scenarios where data must be processed sequentially or accessed in a specific arrangement.
+ Efficient Access: Direct indexing or traversal capabilities of linear structures allow for quick and convenient access to elements.
+ Insertion and Deletion: Linear structures provide efficient methods for adding and removing elements, which is crucial for dynamic data manipulation.
+ Memory Optimization: Linear structures allocate memory contiguously, optimizing memory usage and access efficiency.

#### Real-world Examples of Linear Data Structure:
1. Arrays:
   + Grocery Shopping List: Managing your shopping list with each item corresponding to an array index simplifies adding, removing, and checking off items.
   + Image Pixels: In digital images, arrays store pixel values, allowing manipulation and editing of pictures by altering individual pixel colours.
2. Linked Lists:
   + Music Playlist: Linked lists are suitable for creating playlists, where songs are nodes connected in a sequence, allowing easy rearrangement and modification.
   + Train Cars: Linked lists can represent train cars linked together, enabling efficient addition and removal of cars without affecting the entire train.  
3. Stacks:
   + Undo Feature: In software applications, stacks manage to undo operations, enabling users to reverse actions in the order they were performed.
   + Plate Stacking: Plates stacked on top of each other represent a real-world example of a stack, where the last plate placed is the first one taken.
4. Queues:
   + Cafeteria Line: Queues model waiting in line at a cafeteria, where the first person in line is served first, maintaining order and fairness.
   + Ticket Counter: Waiting in line to purchase tickets, like at a cinema or an event, follows the queue concept.   
5. Deques (Double-Ended Queues):
   + Sliding Glass Doors: Deques are similar to sliding glass doors at entrances, allowing people to enter or exit from both sides.
   + Printing and Scanning: Deques mimic the process of loading and unloading papers for printing and scanning, as both ends are accessible.

## Non-Linear Data Structures
Non-linear data structures do not follow a sequential order; each element can connect to multiple elements, forming complex relationships.
1. Tree: A hierarchical structure with nodes connected by edges, commonly used for organizing hierarchical data like file systems.
2. Graph: A collection of nodes connected by edges, allowing versatile representation of relationships between various entities.
3. Heap: A specialized tree-based structure that satisfies the heap property, often used in priority queues and memory allocation.

#### The Need for Non-Linear Data Structures
+ Complex Relationships:
    Non-linear structures represent intricate relationships between elements, suitable for scenarios with intricate connections.
+ Hierarchical Organization: 
    Trees organize data hierarchically, making them ideal for structures like company organization charts.
+ Graph-based Modeling:
    Graphs enable modelling of various real-world networks, from social connections to computer networks.
+ Efficient Priority Management: 
        Heaps efficiently manage priority-based operations, such as extracting the highest-priority element.

#### Real-world Examples of Non-Linear Data Structures:
1. Tree:
    + File System: Organizing files in a hierarchical structure mirrors the tree concept, with directories as nodes and files as leaves.
    + Family Genealogy: Representing family relationships, like a family tree, illustrates the hierarchical nature of tree structures.
2. Graph:
    + Social Networks: Social media platforms model users and their connections using graph structures to facilitate friend suggestions.
    + Road Networks: Maps utilize graphs to represent roads and intersections, helping navigation systems find the shortest routes.
3. Heap:
    + Priority Queue: A hospital's patient queue can be modeled using a heap, with patients ordered by priority for efficient treatment.
    + Memory Allocation: The memory heap in programming languages allocates memory dynamically, utilizing heap data structure principles.

---

# Classification of Algorithm
There are many ways of classifying algorithms and a few of them are shown below:
+ Implementation Method
+ Design Method
+ Other Classifications

Classification by Implementation Method:

1. Recursion or Iteration
A recursive algorithm is one that calls itself repeatedly until a base condition is satisfied. It is a common method used in functional programming languages like C, C++, etc.
Iterative algorithms use constructs like loops and sometimes other data structures like stacks and queues to solve the problems.
Some problems are suited for recursive and others are suited for iterative. For example, the Towers of Hanoi problem can be easily understood in recursive implementation. Every recursive version has an iterative version and vice versa.

2. Procedural or Declarative (non-Procedural)-
In declarative programming languages, we say what we want without having to say how to do it.
With procedural programming, we have to specify the exact steps to get the result. For example, SQL is more declarative than procedural, because the queries don’t specify the steps to produce the result. Examples of procedural languages include C, PHP, and PERL.

3. Serial or Parallel or Distributed-
In general, while discussing the algorithms we assume that computers execute one instruction at a time. These are called serial algorithms.
Parallel algorithms take advantage of computer architectures to process several instructions at a time. They divide the problem into subproblems and serve them to several processors or threads. Iterative algorithms are generally parallelized.
If the parallel algorithms are distributed to different machines then we call such algorithms distributed algorithms.

4. Deterministic or Non-Deterministic-
Deterministic algorithms solve the problem with a predefined process, whereas non-deterministic algorithms guess the best solution at each step through the use of heuristics.

5. Exact or Approximate-
The algorithms for which we are able to find the optimal solutions are called exact algorithms. In computer science, if we do not have the optimal solution, we give approximation algorithms.
Approximation algorithms are generally associated with NP-hard problems.

#### Design Method:

Another way of classifying algorithms is by their design method.

#### 1. Greedy Method
>
Greedy algorithms work in stages.
In each stage, a decision is made that is good at that point, without bothering about the future consequences. Generally, this means that some local best is chosen. It assumes that the local best selection also makes for the global optimal solution.

#### 2. Divide and Conquer
>
The Divide and Conquer strategy solve a problem by:
- Divide: Breaking the problem into subproblems that are themselves smaller instances of the same type of problem.
- Recursion: Recursively solving these subproblems.
- Conquer: Appropriately combining their answers.
Examples: merge sort and binary search algorithms.

#### 3. Dynamic Programming
>
Dynamic programming (DP) and memorization work together. The difference between DP and divide and conquer is that in the case of the latter there is no dependency among the subproblems, whereas in DP there will be an overlap of subproblems. By using memorization [maintaining a table for already solved sub problems], DP reduces the exponential complexity to polynomial complexity (O(n2), O(n3), etc.) for many problems. The difference between dynamic programming and recursion is in the memorization of recursive calls. When subproblems are independent and if there is no repetition, memorization does not. Hence dynamic programming is not a solution for all problems.
By using memorization [maintaining a table of subproblems already solved], dynamic programming reduces the complexity from exponential to polynomial.

#### 4. Linear Programming 
>
In linear programming, there are inequalities in terms of inputs and maximizing (or minimizing) some linear function of the inputs.
Many problems (example: maximum flow for directed graphs) can be discussed using linear programming.

#### 5. Reduction (Transform and Conquer)
>
In this method, we solve a difficult problem by transforming it into a known problem for which we have asymptotically optimal algorithms. In this method, the goal is to find a reducing algorithm whose complexity is not dominated by the resulting reduced algorithms. For example, the selection algorithm for finding the median in a list involves first sorting the list and then finding out the middle element in the sorted list. These techniques are also called transform and conquer.


# Problem Solving Real Life - Leetcode Roadmap
<img width="723" height="656" alt="Screenshot 2025-08-26 at 3 20 35 PM" src="https://github.com/user-attachments/assets/393a0812-4631-44ff-80fb-fb7882ea8d75" />

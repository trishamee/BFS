# Trisha Mae Beleta
# Romania Problem
# Breadth First Search

# new edit, did it work?

#Defining node
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

# Operators

def initial_state(start, problem):
    for node in problem:
        if start.name == node.name:
            return [start]
    return []

def remove_front(nodes):
    actual_node = nodes.pop(0)
    actual_node.visited = True

    return actual_node

def goal_test(node, target):
    return node.name == target.name

def queueing_fn(nodes, actual_node):
    for n in actual_node.adjacency_list: #expand the tree
        if not n.visited:
            n.visited = True
            nodes.append(n)
    return nodes

def is_empty(frontier):
    return len(frontier) == 0

def reset_visited():
    for node in problem:
        node.visited = False


# creating nodes for each City

node1 = Node("Oradea")
node2 = Node("Zerind")
node3 = Node("Arad")
node4 = Node("Timisoara")
node5 = Node("Sibiu")
node6 = Node("Lugoj")
node7 = Node("Mehadia")
node8 = Node("Dobreta")
node9 = Node("Fagaras")
node10 = Node("Rimnicu Vilcea")
node11 = Node("Pitesti")
node12 = Node("Craiova")
node13 = Node("Neamt")
node14 = Node("Bucharest")
node15 = Node("Giurgiu")
node16 = Node("lasi")
node17 = Node("Vaslui")
node18 = Node("Urziceni")
node19 = Node("Hirsova")
node20 = Node("Eforie")

# Connecting adjacent nodes

#arad
node3.adjacency_list.append(node2)
node3.adjacency_list.append(node5)
node3.adjacency_list.append(node4)
#Zerind
node2.adjacency_list.append(node1)
#Sibiu
node5.adjacency_list.append(node9)
node5.adjacency_list.append(node10)
#Timisoara
node4.adjacency_list.append(node6)
#Oradea
node1.adjacency_list.append(node5)
#Fagaras
node9.adjacency_list.append(node14)
#Rimnicu Vilcea
node10.adjacency_list.append(node11)
node10.adjacency_list.append(node12)
##Lugoj
node6.adjacency_list.append(node7)
#Mehadia
node7.adjacency_list.append(node8)
#Dobreta
node8.adjacency_list.append(node12)
#Craiova
node12.adjacency_list.append(node11)
#Pitesti
node11.adjacency_list.append(node14)
#Bucharest
node14.adjacency_list.append(node15)
node14.adjacency_list.append(node18)
#Urziceni
node18.adjacency_list.append(node19)
node18.adjacency_list.append(node17)
#Vaslui
node17.adjacency_list.append(node16)
#lasi
node16.adjacency_list.append(node13)
#Hirsova
node19.adjacency_list.append(node20)

# Define the problem
problem = []
problem.append(node1)
problem.append(node2)
problem.append(node3)
problem.append(node4)
problem.append(node5)
problem.append(node6)
problem.append(node7)
problem.append(node8)
problem.append(node9)
problem.append(node10)
problem.append(node11)
problem.append(node12)
problem.append(node13)
problem.append(node14)
problem.append(node15)
problem.append(node16)
problem.append(node17)
problem.append(node18)
problem.append(node19)
problem.append(node20)


# Implementing BFS
def breadth_first_search(start_node, target_node):
    frontier = initial_state(start_node, problem)

    while True:
        if is_empty(frontier):
            print("Failure in Search")
            return

        node = remove_front(frontier)

        print(node.name)

        if goal_test(node, target_node):
            print("Found " + node.name)
            return

        nodes = queueing_fn(frontier, node)

# Searching for Bucharest
breadth_first_search(node3, node14)

# ...
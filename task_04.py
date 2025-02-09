import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="green"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(arr, is_max_heap=False):  
    heap = [-x if is_max_heap else x for x in arr]
    heapq.heapify(heap)
    heap = [-x if is_max_heap else x for x in heap]  
    nodes = [Node(heap[i]) for i in range(len(heap))] #створюємо вузли
    
    for i in range(len(heap)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(heap):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap):
            nodes[i].right = nodes[right_idx]   
    return nodes[0] if nodes else None #повертаємо корінь

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_heap_tree(arr, is_max_heap=False): #cтворюємо дерево із бінарної купи  
    root = build_heap_tree(arr, is_max_heap)
    if not root:
        print("Купа порожня")
        return

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=10)
    plt.show()


arr = [10, 3, 5, 1, 7, 8, 2]

print("Мінімальна купа:")
draw_heap_tree(arr, is_max_heap=False)

print("Максимальна-купа:")
draw_heap_tree(arr, is_max_heap=True)

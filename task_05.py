'''Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.'''

import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque
from typing import Optional, List

class Node:
    def __init__(self, key: int):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val: int = key
        self.id: str = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: dict, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

def generate_colors(n: int) -> List[str]:
    cmap = plt.get_cmap("Blues")
    return [mcolors.to_hex(cmap(i / (n + 1))) for i in range(1, n + 1)]

def traverse_and_visualize(root: Node, mode: str = "DFS"):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)  
    nodes = []
    if mode == "DFS":
        def dfs(node: Optional[Node]):
            if node:
                nodes.append(node)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
    else:  #BFS
        queue = deque([root])
        while queue:
            node = queue.popleft()
            nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    colors = generate_colors(len(nodes))
    
    for i, node in enumerate(nodes):
        plt.figure(figsize=(8, 5))
        labels = {n[0]: n[1]['label'] for n in tree.nodes(data=True)}
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, 
                node_color=[colors[i] if n == node.id else "#cccccc" for n in tree.nodes])
        plt.title(f"{mode} Step {i + 1}: Visiting Node {node.val}")
        plt.show()

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

traverse_and_visualize(root, "DFS")
traverse_and_visualize(root, "BFS")

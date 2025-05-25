# Grafy pip install networkx
import networkx as nx
import matplotlib.pyplot as plt

# a) Tworzymy graf nieskierowany z minimum 6 wierzchołkami
graf = nx.Graph()
graf.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('C', 'E'),
    ('E', 'F'),
    ('D', 'F')
])

# b) Narysuj graf
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(graf)  # automatyczne rozmieszczenie wierzchołków
nx.draw(
    graf,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=800,
    font_size=14
)

# c) Oznaczenia etykiet na wykresie
edge_labels = {(u, v): f'{u}-{v}' for u, v in graf.edges()}
nx.draw_networkx_edge_labels(
    graf,
    pos,
    edge_labels=edge_labels,
    font_color='red',
    font_size=12
)

plt.title('Graf nieskierowany z 6 wierzchołkami')
plt.axis('off')
plt.tight_layout()
plt.show()

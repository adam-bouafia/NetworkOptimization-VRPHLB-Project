import networkx as nx
import random

# Create a new directed graph
G = nx.DiGraph()

# Add nodes with attributes
# Add depot
G.add_node(0, label="Depot", type="depot", x=random.uniform(0, 100), y=random.uniform(0, 100))

# Add customers
for i in range(1, 31):  # Increase the number of customers to 30
    earliest_time = random.randint(8, 10)
    latest_time = random.randint(11, 12)
    G.add_node(i, label=f"Customer {i}", type="customer", demand=random.randint(1, 5), earliest=earliest_time, latest=latest_time, x=random.uniform(0, 100), y=random.uniform(0, 100))

# Add locker boxes
for i in range(31, 41):  # Increase the number of locker boxes to 10
    G.add_node(i, label=f"Locker {i-30}", type="locker", capacity=random.randint(10, 20), x=random.uniform(0, 100), y=random.uniform(0, 100))

# Add edges with random weights
for i in G.nodes():
    for j in G.nodes():
        if i != j:
            G.add_edge(i, j, cost=random.uniform(1.0, 10.0))

# Save to GraphML file
graphml_file_path = "vrphlb_graph.graphml"
nx.write_graphml(G, graphml_file_path)

# Verify the content of the generated GraphML file
with open(graphml_file_path, 'r') as f:
    content = f.read()
    print(content)
# Vehicle Routing Problem with Heterogeneous Locker Boxes (VRPHLB)

This repository contains the project for the course **Data Analytics and Data Driven Decision** at Università degli Studi dell'Aquila (Univaq). The project involves the implementation of the Vehicle Routing Problem with Heterogeneous Locker Boxes (VRPHLB) using Mixed-Integer Linear Programming (MILP).

## Table of Contents
- [Introduction](#introduction)
- [Folder Structure](#folder-structure)
- [Mathematical Model](#mathematical-model)
  - [Decision Variables](#decision-variables)
  - [Objective Function](#objective-function)
  - [Constraints](#constraints)
  - [Discussion on MILP](#discussion-on-milp)
- [Data Generation](#data-generation)
- [Implementation and Solution](#implementation-and-solution)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction

The Vehicle Routing Problem with Heterogeneous Locker Boxes (VRPHLB) is an extension of the classical Vehicle Routing Problem (VRP). In VRPHLB, parcels can be delivered to customers' homes or to locker boxes, which act as intermediate delivery points. This model aims to optimize the last-mile delivery process by incorporating alternative delivery points, enhancing logistic efficiency, and improving customer convenience.

**Author**: Adam Bouafia  
**Matricula**: 293137  
**Email**: [adam.bouafia@student.univaq.it](mailto:adam.bouafia@student.univaq.it)  
**Course**: Data Analytics and Data Driven Decision  
**Professors**: Fabrizio Rossi, Andrea Manno  
**Date**: June 2024  

## Folder Structure

- `.ipynb_checkpoints/` - Jupyter Notebook checkpoints.
- `Latex Presentation/` - LaTeX source files for the presentation.
- `Notebook Including GML file/` - Jupyter Notebooks including the generated GML files.
- `PDF Presentation/` - PDF version of the presentation.
- `Scientific Paper for the VRPHLB/` - Scientific paper detailing the VRPHLB.
- `VRPHLB GML code Generator/` - Code for generating the GraphML files for the VRPHLB.

## Mathematical Model

### Decision Variables

- \( x_{ij}^v \): Binary variable indicating if vehicle \( v \) travels directly from node \( i \) to node \( j \).
- \( y_{ik}^v \): Binary variable indicating if customer \( i \) is served at locker box station \( k \) by vehicle \( v \).
- \( z_i^v \): Binary variable indicating if customer \( i \) is served at home.
- \( S_i \): Continuous variable for the service start time at node \( i \).

### Objective Function

The objective is to minimize the total travel distance and compensation costs for using locker boxes:
\[
\min \sum_{i \in N} \sum_{j \in N} \sum_{v \in V} d_{ij} x_{ij}^v + \sum_{i \in N} \sum_{k \in B_i} \sum_{v \in V} c y_{ik}^v
\]

### Constraints

1. **Route Continuity**: Ensures that if a vehicle enters a node, it must leave the node:
\[
\sum_{j \in N \setminus \{i\}} x_{ij}^v = \sum_{j \in N \setminus \{i\}} x_{ji}^v \quad \forall i \in N, \forall v \in V
\]

2. **Vehicle Usage**: Ensures that each vehicle is used at most once:
\[
\sum_{j \in N \setminus \{0\}} x_{0j}^v \leq 1 \quad \forall v \in V
\]

3. **Customer Service**: Ensures that each customer is served either at home or at a locker box:
\[
\sum_{v \in V} \sum_{k \in B_i} y_{ik}^v + \sum_{v \in V} z_i^v = 1 \quad \forall i \in C
\]

4. **Locker Box Capacity**: Ensures that the total demand served at a locker box does not exceed its capacity:
\[
\sum_{i \in C} \sum_{v \in V} q_i y_{ik}^v \leq Q_k \quad \forall k \in B
\]

5. **Time Windows**: Ensures that the service starts within the specified time window:
\[
E_i \sum_{j \in N} \sum_{v \in V} x_{ij}^v \leq S_i \leq L_i \sum_{j \in N} \sum_{v \in V} x_{ij}^v \quad \forall i \in N
\]

6. **Service Time Continuity**: Ensures continuity in service times:
\[
S_i + s_i + d_{ij} - M(1 - x_{ij}^v) \leq S_j \quad \forall i, j \in N, \forall v \in V
\]

### Discussion on MILP

Mixed-Integer Linear Programming (MILP) is a powerful mathematical optimization technique that is widely used for solving combinatorial optimization problems, such as the VRPHLB. MILP models consist of linear objective functions and linear constraints, with some variables constrained to be integer values.

The VRPHLB is particularly suited for MILP due to the following reasons:
- **Binary Variables**: The decision variables \( x_{ij}^v \), \( y_{ik}^v \), and \( z_i^v \) are binary, representing whether a vehicle travels between nodes, serves a customer at a locker box, or serves a customer at home, respectively. MILP handles binary variables efficiently.
- **Complex Constraints**: The problem involves multiple constraints, including route continuity, vehicle usage, customer service, locker box capacity, and time windows. MILP allows the inclusion of such complex constraints in a structured manner.
- **Optimality**: MILP solvers, like Gurobi, provide optimal solutions within reasonable computational times for moderately sized instances, ensuring that the best possible routes and locker box assignments are found.

MILP was chosen for this project due to its ability to model the VRPHLB accurately and its effectiveness in finding optimal solutions for complex optimization problems.

## Data Generation

To test our model, we generated a complex GraphML file representing the problem. This file includes nodes representing the depot, customers, and locker boxes, as well as edges with associated travel costs.

```python
import networkx as nx
import random

# Create a new directed graph
G = nx.DiGraph()

# Add nodes with attributes
# Add depot
G.add_node(0, label="Depot", type="depot", x=random.uniform(0, 100), y=random.uniform(0, 100))

# Add customers
for i in range(1, 31): 
    earliest_time = random.randint(8, 10)
    latest_time = random.randint(11, 12)
    G.add_node(i, label=f"Customer {i}", type="customer", demand=random.randint(1, 5), earliest=earliest_time, latest=latest_time, x=random.uniform(0, 100), y=random.uniform(0, 100))

# Add locker boxes
for i in range(31, 41): 
    G.add_node(i, label=f"Locker {i-30}", type="locker", capacity=random.randint(10, 20), x=random.uniform(0, 100), y=random.uniform(0, 100))

# Add edges with random weights
for i in G.nodes():
    for j in G.nodes():
        if i != j:
            G.add_edge(i, j, cost=random.uniform(1.0, 10.0))

# Save to GraphML file
nx.write_graphml(G, "vrphlb_graph.graphml")

#Implementation and Solution

## The model was implemented using Gurobi, a powerful optimization solver. Below are the steps for implementing and solving the VRPHLB.

import networkx as nx
import matplotlib.pyplot as plt

class args:
    filename = 'vrphlb_graph.graphml'
    scale = 50
    figsize = (10,10)

def DrawInitG(G, withedges=False):
    plt.figure(figsize=args.figsize)
    pos = {i:(G.nodes[i]['x'], G.nodes[i]['y']) for i in G.nodes()}
    nx.draw_networkx_nodes(G, pos=pos, node_shape='o', node_size=600, node_color='red')
    nx.draw_networkx_labels(G, pos=pos, font_color='w', font_size=12)
    if withedges:
        nx.draw_networkx_edges(G, pos=pos, alpha=1.0)
        labels = {(i,j):G.get_edge_data(i,j,'cost').get('cost') for i,j in G.edges()}
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
    plt.axis('off')
    plt.show()

def DrawSol(G, x):
    plt.figure(figsize=args.figsize)
    pos = {i:(G.nodes[i]['x'], G.nodes[i]['y']) for i in G.nodes()}
    nx.draw_networkx_nodes(G, pos=pos, node_shape='o', node_size=600, node_color='red', label=[G.nodes()])
    nx.draw_networkx_labels(G, pos=pos, font_color='w', font_size=12)
    for u,v in G.edges():
        if x[u,v].x > 0.01 and x[u,v].x < 0.9:
            nx.draw_networkx_edges(G, pos=pos, edgelist=[(u,v)], edge_color='r')
            nx.draw_networkx_edge_labels(G, pos=pos, edge_labels={(u,v):'{:.2f}'.format(x[u,v].x)})
        if x[u,v].x > 0.9:
            nx.draw_networkx_edges(G, pos=pos, edgelist=[(u,v)], edge_color='k')
    plt.axis('off')
    plt.show()

args.filename = "vrphlb_graph.graphml"
args.figsize = 10,20

basename = os.path.splitext(args.filename)[0]
G = nx.read_graphml(args.filename, node_type=int)

print("G has", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges")

G = nx.convert_node_labels_to_integers(G, first_label=0, label_attribute='old')

G.nodes(data=True)
pos = {i:(G.nodes[i]['x'] * args.scale, G.nodes[i]['y'] * args.scale) for i in G.nodes()}

DrawInitG(G)

DrawSol(G,x)

```

## Results
After running the model, the optimal routes and locker box assignments were visualized to illustrate the solution. The results showed a significant improvement in delivery efficiency by utilizing locker boxes.

## Conclusion
The implementation of the VRPHLB using MILP and Gurobi demonstrates the potential for optimizing last-mile delivery through the use of locker boxes. This approach not only reduces delivery costs but also increases customer convenience. Future work could explore dynamic locker box capacities and real-time route adjustments.

## References
Grabenschweiger, J., Doerner, K. F., Hartl, R. F., & Savelsbergh, M. W. P. (2021). The vehicle routing problem with heterogeneous locker boxes. Central European Journal of Operations Research, 29, 113–142. https://doi.org/10.1007/s10100-020-00725-2

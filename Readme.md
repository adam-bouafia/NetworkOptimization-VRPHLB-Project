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

![Mathematical Model](https://imgur.com/a/DivNgtG)

### Discussion on MILP

Mixed-Integer Linear Programming (MILP) is a powerful mathematical optimization technique that is widely used for solving combinatorial optimization problems, such as the VRPHLB. MILP models consist of linear objective functions and linear constraints, with some variables constrained to be integer values.

The VRPHLB is particularly suited for MILP due to the following reasons:
- **Binary Variables**: The decision variables \( x_{ij}^v \), \( y_{ik}^v \), and \( z_i^v \) are binary, representing whether a vehicle travels between nodes, serves a customer at a locker box, or serves a customer at home, respectively. MILP handles binary variables efficiently.
- **Complex Constraints**: The problem involves multiple constraints, including route continuity, vehicle usage, customer service, locker box capacity, and time windows. MILP allows the inclusion of such complex constraints in a structured manner.
- **Optimality**: MILP solvers, like Gurobi, provide optimal solutions within reasonable computational times for moderately sized instances, ensuring that the best possible routes and locker box assignments are found.

MILP was chosen for this project due to its ability to model the VRPHLB accurately and its effectiveness in finding optimal solutions for complex optimization problems.

## Results
After running the model, the optimal routes and locker box assignments were visualized to illustrate the solution. The results showed a significant improvement in delivery efficiency by utilizing locker boxes.

## Conclusion
The implementation of the VRPHLB using MILP and Gurobi demonstrates the potential for optimizing last-mile delivery through the use of locker boxes. This approach not only reduces delivery costs but also increases customer convenience. Future work could explore dynamic locker box capacities and real-time route adjustments.

## References
Grabenschweiger, J., Doerner, K. F., Hartl, R. F., & Savelsbergh, M. W. P. (2021). The vehicle routing problem with heterogeneous locker boxes. Central European Journal of Operations Research, 29, 113–142. https://doi.org/10.1007/s10100-020-00725-2

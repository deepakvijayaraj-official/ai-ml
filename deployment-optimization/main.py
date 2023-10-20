from pulp import LpProblem, LpVariable, LpMinimize, LpConstraint, lpSum

# Define the problem as a linear programming (LP) problem
problem = LpProblem("Deployment_Optimization", LpMinimize)

# Define the number of resource types
num_resources = 2

# Define the costs for each resource type
resource_costs = [100, 150]  # Cost per unit of each resource type

# Define the demand for each resource type
demand = [200, 300]  # Demand for each resource type

# Define the maximum available units for each resource type
max_resources = [500, 400]  # Maximum available units for each resource type

# Define the decision variables
resource_vars = [LpVariable(f"Resource_{i}", lowBound=0, upBound=max_resources[i], cat='Integer') for i in range(num_resources)]

# Define the objective function (minimize cost)
problem += lpSum([resource_vars[i] * resource_costs[i] for i in range(num_resources)])

# Define demand constraints
for i in range(num_resources):
    problem += resource_vars[i] >= demand[i]

# Define maximum resource constraints
for i in range(num_resources):
    problem += resource_vars[i] <= max_resources[i]

# Solve the optimization problem
problem.solve()

# Print the results
if problem.status == 1:  # 1 indicates an optimal solution was found
    print("Optimal Solution:")
    for i, resource_var in enumerate(resource_vars):
        print(f"Resource_{i}: {resource_var.varValue} units")
    print(f"Total Cost: ${problem.objective.value()}")
else:
    print("No optimal solution found.")

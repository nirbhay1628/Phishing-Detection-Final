import pulp

# Define the model
model = pulp.LpProblem("Solar_Grid_Distribution", pulp.LpMinimize)

# Variables
x_PA = pulp.LpVariable('x_PA', lowBound=0)
x_PB = pulp.LpVariable('x_PB', lowBound=0)
x_PC = pulp.LpVariable('x_PC', lowBound=0)
x_PD = pulp.LpVariable('x_PD', lowBound=0)
x_P2A = pulp.LpVariable('x_P2A', lowBound=0)
x_P2B = pulp.LpVariable('x_P2B', lowBound=0)
x_P2C = pulp.LpVariable('x_P2C', lowBound=0)
x_P2D = pulp.LpVariable('x_P2D', lowBound=0)

# Objective
model += (
    2*x_PA + 3*x_PB + 4*x_PC + 5*x_PD +
    3*x_P2A + 1*x_P2B + 2*x_P2C + 4*x_P2D
), "Total Transmission Cost"

# Constraints
model += x_PA + x_PB + x_PC + x_PD <= 200, "P1 Supply"
model += x_P2A + x_P2B + x_P2C + x_P2D <= 180, "P2 Supply"
model += x_PA + x_P2A >= 120, "Demand A"
model += x_PB + x_P2B >= 100, "Demand B"
model += x_PC + x_P2C >= 80, "Demand C"
model += x_PD + x_P2D >= 60, "Demand D"

# Solve
model.solve()

# Results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Transmission Plan:")
for var in model.variables():
    print(f"{var.name} = {var.varValue}")
print("Minimum Transmission Cost =", pulp.value(model.objective))

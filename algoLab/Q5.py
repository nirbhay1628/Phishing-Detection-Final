import pulp

# Define the model
model = pulp.LpProblem("Emergency_Fuel_Allocation", pulp.LpMaximize)

# Variables
x = pulp.LpVariable('CityX', lowBound=0)
y = pulp.LpVariable('CityY', lowBound=0)
z = pulp.LpVariable('CityZ', lowBound=0)

# Objective
model += 40*x + 50*y + 60*z, "Total Profit"

# Constraints
model += x + y + z <= 500, "Depot Supply"
model += x <= 180, "CityX Capacity"
model += y <= 200, "CityY Capacity"
model += z <= 150, "CityZ Capacity"

# Solve
model.solve()

# Results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Fuel Allocation:")
for var in model.variables():
    print(f"{var.name} = {var.varValue}")
print("Maximum Profit =", pulp.value(model.objective))

import pulp

# Define the model
model = pulp.LpProblem("Airline_Crew_Scheduling", pulp.LpMinimize)

# Variables
x1A = pulp.LpVariable('x1A', lowBound=0)
x2A = pulp.LpVariable('x2A', lowBound=0)
x3A = pulp.LpVariable('x3A', lowBound=0)
x2B = pulp.LpVariable('x2B', lowBound=0)
x3B = pulp.LpVariable('x3B', lowBound=0)

# Objective
model += (
    12000 * (x1A + x2A + x3A) +
    9000 * (x2B + x3B)
), "Total Crew Cost"

# Constraints
model += x1A >= 5, "Flight1 Requirement"
model += x2A + x2B >= 6, "Flight2 Requirement"
model += x3A + x3B >= 4, "Flight3 Requirement"
model += x1A + x2A + x3A <= 10, "Type A Availability"
model += x2B + x3B <= 8, "Type B Availability"

# Solve
model.solve()

# Results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Crew Assignment:")
for var in model.variables():
    print(f"{var.name} = {var.varValue}")
print("Minimum Crew Cost =", pulp.value(model.objective))

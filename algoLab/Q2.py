import pulp

# Define the model
model = pulp.LpProblem("Workforce_Allocation", pulp.LpMinimize)

# Variables
x1 = pulp.LpVariable('Morning', lowBound=0)
x2 = pulp.LpVariable('Afternoon', lowBound=0)
x3 = pulp.LpVariable('Night', lowBound=0)
c1 = pulp.LpVariable('Contract_Morning', lowBound=0)
c2 = pulp.LpVariable('Contract_Afternoon', lowBound=0)
c3 = pulp.LpVariable('Contract_Night', lowBound=0)

# Objective
model += 500*x1 + 450*x2 + 600*x3 + 700*(c1 + c2 + c3), "Total Cost"

# Constraints
model += x1 >= 6, "Morning Requirement"
model += x2 >= 5, "Afternoon Requirement"
model += x3 >= 4, "Night Requirement"
model += x1 + x2 + x3 - (c1 + c2 + c3) <= 12, "Permanent Worker Constraint"

# Solve
model.solve()

# Results
print("Status:", pulp.LpStatus[model.status])
print("Optimal Workforce Allocation:")
for var in model.variables():
    print(f"{var.name} = {var.varValue}")
print("Minimum Cost =", pulp.value(model.objective))

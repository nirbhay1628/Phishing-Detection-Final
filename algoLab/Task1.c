 
# NSGA-II for EV charger placement
import numpy as np
import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import ElementwiseProblem
from pymoo.termination import get_termination
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
 
 
# Demand nodes
nodes = np.array([
    [2.0, 3.0, 30], [5.1, 8.2, 45], [7.0, 2.1, 20],
    [1.5, 10.0, 10], [4.0, 5.0, 35], [8.5, 6.0, 25],
    [9.0, 1.0, 15], [3.0, 7.5, 40], [6.0, 9.0, 50],
    [2.5, 1.0, 12], [5.5, 3.5, 22], [7.5, 8.0, 18],
    [0.5, 5.0, 8], [10.0, 5.0, 28], [4.5, 0.5, 14]
])
sites = np.array([
    [1.0, 2.5, 800, 200], [3.5, 6.0, 950, 180],
    [6.0, 2.0, 700, 210], [8.0, 7.0, 1200, 190],
    [9.0, 0.8, 900, 220], [2.0, 10.0, 850, 170],
    [5.0, 4.5, 880, 185], [7.8, 9.2, 1100, 180],
    [0.8, 6.0, 600, 200], [4.6, 1.2, 760, 205]
])
X, Y, W = nodes[:, 0], nodes[:, 1], nodes[:, 2]
W /= np.sum(W)
site_names = [f"A{i+1}" for i in range(10)]
K = 3
 
 
# Define multi-objective problem
class EVChargingProblem(ElementwiseProblem):
	def __init__(self):
        super().__init__(n_var=10, n_obj=2, n_constr=1, xl=0, xu=1, type_var=bool)
 
 
	def _evaluate(self, x, out, *args, **kwargs):
        selected_sites = sites[x == 1]
 
 
        if selected_sites.shape[0] == 0:
            # Handle the case where no sites are selected
            out["F"] = [np.inf, np.inf]
            out["G"] = [1.0] # Assign a penalty for violating the constraint
            return
 
 
        total_cost = np.sum(selected_sites[:, 2] + selected_sites[:, 3])
        dist = []
        for i in range(len(nodes)):
            d = np.sqrt((selected_sites[:, 0] - X[i])**2 + (selected_sites[:, 1] - Y[i])**2)
            dist.append(np.min(d))
        avg_dist = np.sum(W * np.array(dist))
 
 
        out["F"] = [avg_dist, total_cost]
        out["G"] = [np.sum(x) - K] # Constraint: sum(x) must be equal to K (sum(x) - K = 0)
 
 
problem = EVChargingProblem()
 
 
algorithm = NSGA2(pop_size=100)
termination = get_termination("n_gen", 200)
 
 
res = minimize(problem, algorithm, termination, verbose=True)
 
 
print("\nPareto-optimal Solutions:")
# Check if res.X is not None and has at least 3 solutions
if res.X is not None and len(res.X) >= 3:
	for i in range(3):
        sol = res.X[i]
        chosen = [site_names[j] for j in range(10) if sol[j] == 1]
        print(f"Solution {i+1}: {chosen}, f1={res.F[i][0]:.4f}, f2={res.F[i][1]:.2f}")
elif res.X is not None:
     print("Less than 3 Pareto-optimal solutions found.")
 	for i in range(len(res.X)):
        sol = res.X[i]
        chosen = [site_names[j] for j in range(10) if sol[j] == 1]
        print(f"Solution {i+1}: {chosen}, f1={res.F[i][0]:.4f}, f2={res.F[i][1]:.2f}")
else:
    print("No Pareto-optimal solutions found.")
 
 
 
 
# Pareto front visualization
if res.F is not None:
    Scatter(title="Pareto Front (Cost vs Distance)").add(res.F).show()
else:
    print("No Pareto front to display.")

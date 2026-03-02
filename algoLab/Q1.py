# Q1.py — Final Version (All Graphs on One Page)
import math
import random
import time
import os
from collections import deque
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

random.seed(42)
np.random.seed(42)

# ---------- Problem Data ----------
points = {
    1: (5, 8), 2: (12, 4), 3: (8, 14), 4: (16, 10), 5: (3, 9),
    6: (11, 17), 7: (14, 2), 8: (9, 6), 9: (7, 3), 10: (18, 12),
    11: (2, 7), 12: (10, 15), 13: (6, 11), 14: (17, 5), 15: (4, 4),
    16: (8, 10), 17: (1, 13), 18: (15, 15), 19: (13, 8), 20: (19, 9),
}
ids = list(points.keys())
n = len(ids)

def euclidean(a, b): return math.hypot(a[0]-b[0], a[1]-b[1])

dist = np.zeros((n+1, n+1))
for i in ids:
    for j in ids:
        dist[i, j] = euclidean(points[i], points[j])

def route_length(route):
    return sum(dist[route[i], route[i+1]] for i in range(len(route)-1))

def to_full_route(path): return [1] + path + [1]

# ---------- Greedy ----------
def greedy_from(start=1):
    unvisited = set(ids)
    unvisited.remove(start)
    route = [start]
    while unvisited:
        nxt = min(unvisited, key=lambda x: dist[route[-1], x])
        route.append(nxt)
        unvisited.remove(nxt)
    route.append(start)
    return route, route_length(route)

def greedy_all_starts():
    results = {}
    t0 = time.time()
    for s in ids:
        route, length = greedy_from(s)
        results[s] = (route, length)
    return results, time.time() - t0

greedy_results, greedy_time = greedy_all_starts()
greedy_route, greedy_cost = greedy_results[1]

# ---------- Hill Climbing ----------
def random_route():
    path = ids.copy()
    path.remove(1)
    random.shuffle(path)
    return to_full_route(path)

def two_swap(route, i, j):
    r = route.copy()
    r[i], r[j] = r[j], r[i]
    return r

def hill_climbing(max_iters=5000):
    current = random_route()
    current_cost = route_length(current)
    best = current.copy()
    best_cost = current_cost
    history = [(0, current_cost)]
    improved, it = True, 0
    while improved and it < max_iters:
        improved = False
        it += 1
        best_neighbor, best_neighbor_cost = None, current_cost
        for i in range(1, len(current)-2):
            for j in range(i+1, len(current)-1):
                neighbor = two_swap(current, i, j)
                c = route_length(neighbor)
                if c < best_neighbor_cost:
                    best_neighbor_cost, best_neighbor = c, neighbor
        if best_neighbor and best_neighbor_cost < current_cost:
            current, current_cost = best_neighbor, best_neighbor_cost
            improved = True
            if current_cost < best_cost:
                best, best_cost = current.copy(), current_cost
        history.append((it, current_cost))
    return best, best_cost, history, it, time.time()

hc_best_route, hc_best_cost, hc_history, hc_iters, hc_time = hill_climbing()

# ---------- Simulated Annealing ----------
def simulated_annealing(initial_temp=100, alpha=0.95, iter_per_temp=100, max_iters=10000):
    current = random_route()
    current_cost = route_length(current)
    best, best_cost, T, it = current.copy(), current_cost, initial_temp, 0
    history = [(it, current_cost, T)]
    while T > 0.001 and it < max_iters:
        for _ in range(iter_per_temp):
            it += 1
            i, j = sorted(random.sample(range(1, len(current)-1), 2))
            neighbor = two_swap(current, i, j)
            neighbor_cost = route_length(neighbor)
            delta = neighbor_cost - current_cost
            if delta < 0 or random.random() < math.exp(-delta / T):
                current, current_cost = neighbor, neighbor_cost
                if current_cost < best_cost:
                    best, best_cost = current.copy(), current_cost
            history.append((it, current_cost, T))
            if it >= max_iters: break
        T *= alpha
    return best, best_cost, history, it, time.time()

sa_best_route, sa_best_cost, sa_history, sa_iters, sa_time = simulated_annealing()

# ---------- Tabu Search ----------
def tabu_search(tabu_tenure=7, max_iters=3000):
    current = random_route()
    current_cost = route_length(current)
    best, best_cost, tabu, history = current.copy(), current_cost, deque(maxlen=tabu_tenure), [(0, current_cost)]
    for it in range(1, max_iters+1):
        neighborhood = []
        for i in range(1, len(current)-2):
            for j in range(i+1, len(current)-1):
                move = (i, j)
                if move in tabu: continue
                neighbor = two_swap(current, i, j)
                c = route_length(neighbor)
                neighborhood.append((c, move, neighbor))
        if not neighborhood: break
        neighborhood.sort(key=lambda x: x[0])
        best_neighbor_cost, best_move, best_neighbor = neighborhood[0]
        current, current_cost = best_neighbor, best_neighbor_cost
        tabu.append(best_move)
        if current_cost < best_cost:
            best, best_cost = current.copy(), current_cost
        history.append((it, current_cost))
    return best, best_cost, history, it, time.time()

ts_best_route, ts_best_cost, ts_history, ts_iters, ts_time = tabu_search()

# ---------- Summary ----------
results = {
    "Greedy": {"route": greedy_route, "cost": greedy_cost, "time": greedy_time, "iters": "-"},
    "Hill Climbing": {"route": hc_best_route, "cost": hc_best_cost, "time": hc_time, "iters": hc_iters},
    "Simulated Annealing": {"route": sa_best_route, "cost": sa_best_cost, "time": sa_time, "iters": sa_iters},
    "Tabu Search": {"route": ts_best_route, "cost": ts_best_cost, "time": ts_time, "iters": ts_iters},
}

print("\nAlgorithm Summary:")
for name, r in results.items():
    print(f"{name}: cost={r['cost']:.3f}, time={r['time']:.3f}s, iters={r['iters']}")

# ---------- Combined Graphs (Single Page) ----------
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.ravel()

# Routes
for i, (algo, res) in enumerate(list(results.items())[:4]):
    xs = [points[p][0] for p in res['route']]
    ys = [points[p][1] for p in res['route']]
    axs[i].plot(xs, ys, marker='o')
    for j, node in enumerate(res['route']):
        axs[i].text(xs[j]+0.2, ys[j]+0.2, str(node), fontsize=8)
    axs[i].set_title(f"{algo} (cost={res['cost']:.2f})")
    axs[i].grid(True)

# Hill Climbing Distance vs Iteration
hc_iters_list = [h[0] for h in hc_history]
hc_costs = [h[1] for h in hc_history]
axs[4].plot(hc_iters_list, hc_costs)
axs[4].set_title("Hill Climbing: Distance vs Iteration")
axs[4].set_xlabel("Iteration")
axs[4].set_ylabel("Distance")
axs[4].grid(True)

# Simulated Annealing Cost vs Iteration
sa_iters_list = [h[0] for h in sa_history]
sa_costs = [h[1] for h in sa_history]
axs[5].plot(sa_iters_list, sa_costs)
axs[5].set_title("Simulated Annealing: Cost vs Iteration")
axs[5].set_xlabel("Iteration")
axs[5].set_ylabel("Cost")
axs[5].grid(True)

plt.tight_layout()

outdir = os.path.join(os.getcwd(), "tsp_results")
os.makedirs(outdir, exist_ok=True)
plt.savefig(os.path.join(outdir, "all_combined_graphs.png"), dpi=200)
plt.show()

print(f"\n✅ All graphs and summary saved in: {outdir}")

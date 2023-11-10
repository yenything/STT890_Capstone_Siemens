import numpy as np
import csv
import os
 
 
def get_relation(ind_a, ind_b):
    return Dominator.get_relation(ind_a.F, ind_b.F, ind_a.CV[0], ind_b.CV[0])
 
 
class Dominator:
 
    @staticmethod
    def get_relation(a, b, cva=None, cvb=None):
 
        if cva is not None and cvb is not None:
            if cva < cvb:
                return 1
            elif cvb < cva:
                return -1
 
        val = 0
        for i in range(len(a)):
            if a[i] < b[i]:
                # indifferent because once better and once worse
                if val == -1:
                    return 0
                val = 1
            elif b[i] < a[i]:
                # indifferent because once better and once worse
                if val == 1:
                    return 0
                val = -1
        return val
 
    @staticmethod
    def calc_domination_matrix_loop(F, G):
        n = F.shape[0]
        CV = np.sum(G * (G > 0).astype(float), axis=1)
        M = np.zeros((n, n))
        for i in range(n):
            for j in range(i + 1, n):
                M[i, j] = Dominator.get_relation(F[i, :], F[j, :], CV[i], CV[j])
                M[j, i] = -M[i, j]
 
        return M
 
    @staticmethod
    def calc_domination_matrix(F, _F=None, epsilon=0.0):
 
        if _F is None:
            _F = F
 
        # look at the obj for dom
        n = F.shape[0]
        m = _F.shape[0]
 
        L = np.repeat(F, m, axis=0)
        R = np.tile(_F, (n, 1))
 
        smaller = np.reshape(np.any(L + epsilon < R, axis=1), (n, m))
        larger = np.reshape(np.any(L > R + epsilon, axis=1), (n, m))
 
        M = np.logical_and(smaller, np.logical_not(larger)) * 1 \
            + np.logical_and(larger, np.logical_not(smaller)) * -1
 
        # if cv equal then look at dom
        # M = constr + (constr == 0) * dom
 
        return M
 
 
def fast_non_dominated_sort(F, **kwargs):
    M = Dominator.calc_domination_matrix(F)
 
    # calculate the dominance matrix
    n = M.shape[0]
 
    fronts = []
 
    if n == 0:
        return fronts
 
    # final rank that will be returned
    n_ranked = 0
    ranked = np.zeros(n, dtype=int)
 
    # for each individual a list of all individuals that are dominated by this one
    is_dominating = [[] for _ in range(n)]
 
    # storage for the number of solutions dominated this one
    n_dominated = np.zeros(n)
 
    current_front = []
 
    for i in range(n):
 
        for j in range(i + 1, n):
            rel = M[i, j]
            if rel == 1:
                is_dominating[i].append(j)
                n_dominated[j] += 1
            elif rel == -1:
                is_dominating[j].append(i)
                n_dominated[i] += 1
 
        if n_dominated[i] == 0:
            current_front.append(i)
            ranked[i] = 1.0
            n_ranked += 1
 
    # append the first front to the current front
    fronts.append(current_front)
 
    # while not all solutions are assigned to a pareto front
    while n_ranked < n:
 
        next_front = []
 
        # for each individual in the current front
        for i in current_front:
 
            # all solutions that are dominated by this individuals
            for j in is_dominating[i]:
                n_dominated[j] -= 1
                if n_dominated[j] == 0:
                    next_front.append(j)
                    ranked[j] = 1.0
                    n_ranked += 1
 
        fronts.append(next_front)
        current_front = next_front
 
    return fronts
 
 
class NonDominatedSorting:
 
    def __init__(self, epsilon=None, method="fast_non_dominated_sort") -> None:
        super().__init__()
        self.epsilon = epsilon
        self.method = method
 
    def do(self, F, return_rank=False, only_non_dominated_front=False, n_stop_if_ranked=None, **kwargs):
        F = F.astype(float)
 
        # if not set just set it to a very large values because the cython algorithms do not take None
        if n_stop_if_ranked is None:
            n_stop_if_ranked = int(1e8)
 
        # set the epsilon if it should be set
        if self.epsilon is not None:
            kwargs["epsilon"] = float(self.epsilon)
 
        fronts = fast_non_dominated_sort(F, **kwargs)
 
        # convert to numpy array for each front and filter by n_stop_if_ranked if desired
        _fronts = []
        n_ranked = 0
        for front in fronts:
 
            _fronts.append(np.array(front, dtype=int))
 
            # increment the n_ranked solution counter
            n_ranked += len(front)
 
            # stop if more than this solutions are n_ranked
            if n_ranked >= n_stop_if_ranked:
                break
 
        fronts = _fronts
 
        if only_non_dominated_front:
            return fronts[0]
 
        if return_rank:
            rank = rank_from_fronts(fronts, F.shape[0])
            return fronts, rank
 
        return fronts
 
 
def rank_from_fronts(fronts, n):
    # create the rank array and set values
    rank = np.full(n, 1e16, dtype=int)
    for i, front in enumerate(fronts):
        rank[front] = i
 
    return rank
 
 
# Returns all indices of F that are not dominated by the other objective values
def find_non_dominated(F, _F=None):
    M = Dominator.calc_domination_matrix(F, _F)
    I = np.where(np.all(M >= 0, axis=1))[0]
    return I
 


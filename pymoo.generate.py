from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import numpy as np
import pandas as pd

var_num = 10
problem = get_problem("zdt1", var_num)

algorithm = NSGA2(pop_size=50)
res = minimize(problem,
               algorithm,
               ("n_gen", 100),
               save_history=True,
               seed=1,
               verbose=False)

history = res.history

data_list = []
for entry in history:
    gen = entry.n_gen
    pop = entry.pop
    for ind in pop:
        data_dict = {}
        for i, x in enumerate(ind.X):
            data_dict[f"x{i + 1}"] = x
        data_dict["f1"] = ind.F[0]
        data_dict["f2"] = ind.F[1]
        data_dict["gen"] = gen
        data_dict["RANK"] = np.nan
        data_list.append(data_dict)

df = pd.DataFrame(data_list)
df.to_csv(r'C:\Users\user\Documents\JupyterWork\STT890_PRJ\Siemens_prj\ZDT1_10var100gen.csv')

df_only_objectives = df[["f1", "f2"]]
df_only_objectives.to_csv(r'C:\Users\user\Documents\JupyterWork\STT890_PRJ\Siemens_prj\only_objectives.csv', header=False, index=False)
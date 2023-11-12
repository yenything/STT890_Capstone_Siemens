import numpy as np
import NonDominatedSorting as nds
 
# load csv file
f_data = np.genfromtxt(r'C:\Users\user\Documents\JupyterWork\STT890_PRJ\Siemens_prj\only_objectives.csv', delimiter=',')
 
nds_obj = nds.NonDominatedSorting()
rank_info= nds_obj.do(f_data, return_rank=True)
 
rank_info_array = rank_info[1]
 
np.savetxt(r'C:\Users\user\Documents\JupyterWork\STT890_PRJ\Siemens_prj\rank_info.csv', rank_info_array, fmt='%d')
 
 
print('End')
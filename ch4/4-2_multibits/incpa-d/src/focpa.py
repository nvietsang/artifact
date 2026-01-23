from pearson import pearson_v3
from utils import load_trace_matrix
from model import load_guess_matrix_z
from ranking import ranking_cpa
from tqdm import tqdm
import os
import numpy as np
import pickle

def focpa_v6(config, trace_indexes):
    '''
    '''
    nk = config.nk
    nt = config.nt
    nn = config.nn
    ns = config.ns
    nd = config.nd
    _dtype = config.data_type

    if nn % ns != 0: raise ValueError(f"Number of traces must be a multiple of step")
    basepath = config.path_to_checkpoints

    for delta in range(1<<(nd-1)):
        # Files of checkpoints
        config.path_to_checkpoints = f"{basepath}/{delta}"
        os.makedirs(f"{config.path_to_checkpoints}", exist_ok=True)
        checkpoints = [int(v.split(".")[0]) for v in sorted(os.listdir(config.path_to_checkpoints))
                    if v != ".DS_Store"]
        
        if len(checkpoints) == 0: 
            cpdata = {}
            nn_cp = 0
            s1 = np.zeros(nt, dtype=_dtype)
            s2 = np.zeros(nt, dtype=_dtype)
            s3 = np.zeros(nk, dtype=_dtype)
            s4 = np.zeros(nk, dtype=_dtype)
            s5 = np.zeros((nk,nt), dtype=_dtype)
        else:
            nn_cp = checkpoints[-1]
            with open(f"{config.path_to_checkpoints}/{nn_cp:07d}.pkl", 'rb') as f: 
                cpdata = pickle.load(f)
            if nn <= nn_cp:
                print(f"Already calculated and stored in file of checkpoints")
                print(f"[INFO] Incremental cpa with {nn_cp} traces:")
                ranked_candidates = ranking_cpa(cpdata["rho"], nr=config.nr)
                print(f"[INFO] Ranking key candidate:")
                for i, item in enumerate(ranked_candidates): 
                    print(f"Rank {i:2d}: {item[1]:4d} - {item[0]:.06f}")
                continue
            s1 = cpdata["s1"]
            s2 = cpdata["s2"]
            s3 = cpdata["s3"]
            s4 = cpdata["s4"]
            s5 = cpdata["s5"]
        
        
        # Compute cpa with step
        for i in range((nn-nn_cp)//ns):
            nn_cur = nn_cp+(i+1)*ns
            rho = np.zeros((nk,nt), dtype=_dtype)
            print(f"[INFO] Incremental cpa with {nn_cur} traces:")
            if config.to_shuffle:
                step_indexes = trace_indexes[i*ns:(i+1)*ns]
            else:
                step_indexes = trace_indexes[nn_cp+i*ns:nn_cur]

            # Load HW matrix for all guesses
            if config.selection_function in ["z0", "z1", "z4"]: K = load_guess_matrix_z(config, step_indexes, delta)
            else: raise ValueError('Invalid selection function')
            # print(K)

            # Load matrix of traces
            T = load_trace_matrix(config, step_indexes)
        
            # Run incremental CPA
            for j in tqdm(range(nk)):
                s3[j] += np.sum(K[j])
                s4[j] += np.sum(K[j]**2)

            for i in tqdm(range(nt)):
                s1[i] += np.sum(T[i])
                s2[i] += np.sum(T[i]**2)
                for j in range(nk):
                    s5[j,i] += np.dot(T[i], K[j])
                    rho[j,i] = pearson_v3(nn_cur, s1[i], s2[i], s3[j], s4[j], s5[j,i])

            # Show ranking for key candidates
            ranked_candidates = ranking_cpa(rho, nr=config.nr)
            print(f"[INFO] Ranking key candidate:")
            for i, item in enumerate(ranked_candidates): 
                print(f"Rank {i:2d}: {item[1]:4d} - {item[0]:.06f}")

            # Saving results to file
            cpdata = {"s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5, "rho": rho}
            with open(f"{config.path_to_checkpoints}/{nn_cur:07d}.pkl", 'wb') as f:  
                pickle.dump(cpdata, f)
                
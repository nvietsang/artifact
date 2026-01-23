import os
import pickle
import argparse
import numpy as np
import matplotlib.pyplot as plt
from heapq import heapreplace, heappush
from queue import PriorityQueue

indexes_k0b1z0 = [1, 2, 5, 8, 11, 12, 15, 18, 19, 22, 25, 28, 29, 32, 35, 39, 42, 45, 49, 52, 55, 59, 62]     # 23
indexes_k1b1z1 = [3, 5, 6, 7, 13, 15, 17, 22, 24, 26, 32, 33, 34, 39, 41, 43, 45, 50, 51, 52, 53, 58, 60, 62] # 24

indexes_k0b2z0 = [0, 2, 4, 8, 18, 25, 34, 38, 40, 42, 48, 50, 52, 55] # 14
indexes_k1b2z1 = [5, 7, 15, 17, 19, 21, 23, 25, 33, 35, 40, 42, 51, 53] # 14

indexes_k0b3z0 = [24, 27, 29, 32, 34, 37, 40, 51, 54, 57] # 10
indexes_k1b3z1 = [2, 5, 14, 21, 27, 33, 40, 50, 59]       # 9

indexes_k0b4z0 = [28, 32, 36, 40, 44, 55, 59, 60] # 8
indexes_k1b4z1 = [6, 16, 24, 34, 42, 52, 60]      # 7

class RankingQueue(PriorityQueue):
    def _put(self, item):
        if len(self.queue) < self.maxsize-1:
            heappush(self.queue, item)
        elif item > self.queue[0]:
            heapreplace(self.queue, item)
        else: pass

def ranking_cpa(rho, nr=5):
    q = RankingQueue(nr+1)
    for k, cors in enumerate(rho): q.put((float((np.nanmax(np.abs(cors)))), k))
    return sorted(q.queue, reverse=True)

def postprocess_guess(config, rho, nd, order=1):
    if not config.boost and nd > 1:
        assert order == 1, "Success order must be 1 without boosting"
        return []

    if nd == 1:
        top = np.argsort(rho.max(1).reshape((8,)))[::-1]
        return list(top[:order])


def extract_bit(x, j):
    '''
    :param x: an integer of 64 bits
    :param j: index
    '''
    return (x >> j) & 1

def trim_tuple(x: int, i0, nd, selection_function):
    '''
    :param x: an integer of 64 bits
    '''
    if   selection_function == "z0":
        i1 = (i0 + 19) % 64
        i2 = (i0 + 28) % 64
    elif selection_function == "z1":
        i1 = (i0 + 61) % 64
        i2 = (i0 + 39) % 64
    elif selection_function == "z4":
        i1 = (i0 +  7) % 64
        i2 = (i0 + 41) % 64
    else: raise ValueError

    v2 = 0
    for i in range(nd-1,-1,-1):
        j2 = (i+i2)%64
        b2 = extract_bit(x, j2)
        v2 ^= (b2 << i)

    v1 = 0
    for i in range(nd-1,-1,-1):
        j1 = (i+i1)%64
        b1 = extract_bit(x, j1)
        v1 ^= (b1 << i)

    v0 = 0
    for i in range(nd-1,-1,-1):
        j0 = (i+i0)%64
        b0 = extract_bit(x, j0)
        v0 ^= (b0 << i)        
            
    tup = (v2 << (2*nd)) | (v1 << (nd)) | (v0)
    return tup

def success_rates(config, 
                  target_key, 
                  selection_function, 
                  indexes, 
                  nd,
                  kref,
                  nbtrace_range):

    subkeys_ref = dict()
    for j in indexes:
        subkey = trim_tuple(kref, j, nd, selection_function)
        subkeys_ref[j] = subkey

    successrates = [0] * len(nbtrace_range)
    count = 0

    path_prefix = f"{config.path_to_checkpoints}/{target_key}/{selection_function}/b{nd}"
    for idx in indexes:
        for rep in os.listdir(f"{path_prefix}/{idx:02d}"):
            if ".DS_Store" in rep: continue
            path_to_rep = f"{path_prefix}/{idx:02d}/{rep}"

            for i, nbtr in enumerate(nbtrace_range):
                R = None
                for delta in range(1<<(nd-1)):
                    path_to_file = f"{path_to_rep}/{delta}/{nbtr:07d}.pkl"
                    if not os.path.exists(path_to_file):
                        print(path_to_file)
                        raise FileNotFoundError
                    with open(path_to_file, "rb") as f: cp = pickle.load(f)
                    rho = np.abs(cp["rho"])
                    if R is None: R = rho
                    else: R = np.hstack((R, rho))

                best_guesses = np.argmax(R.max(1).reshape((1<<(3*nd),)))                
                successrates[i] += (subkeys_ref[idx] == int(best_guesses))
                # if not (subkeys_ref[idx] == best_guesses) and nbtr > 5000:
                #     print(idx, nbtr, subkeys_ref[idx], best_guesses)
            count += 1
    return count, successrates

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--path-to-checkpoints', 
                        dest='path_to_checkpoints', 
                        help="Path to the folder of checkpoints",
                        default="outputs/checkpoints4",
                        type=str)
    parser.add_argument("--n-traces",
                        dest="nn",
                        help="Number of traces",
                        default=10000,
                        type=int)
    parser.add_argument("--n-bits-selection-function",
                        dest="nd",
                        help="Number of bits for the selection function",
                        type=int,
                        required=True)
    parser.add_argument("--step",
                        dest="ns",
                        help="Number of traces for each process",
                        default=250,
                        type=int)
    
    
    config = parser.parse_args()

    nn = config.nn
    ns = config.ns
    nd = config.nd
    nbtrace_range = list(range(ns, nn+1, ns))

    # log files and keys for 5 datasets
    checkpoints = ["checkpoints0", "checkpoints1", "checkpoints2", "checkpoints3", "checkpoints4"]
    reference_keys = [
        0xb3a6cca5c31b846c98580f80255ba076,
        0xef24ac286868d507a6b914c005685185,
        0x0ae6d146ead05ee8544b38f062bbcc5d,
        0x4cca238280d800aac424d1367509283c,
        0xa5020b6df76b8f2437d06aa4448cf70f
    ]

    if nd == 1:
        indexes_k0 = indexes_k0b1z0
        indexes_k1 = indexes_k1b1z1
    elif nd == 2:
        indexes_k0 = indexes_k0b2z0
        indexes_k1 = indexes_k1b2z1
    elif nd == 3:
        indexes_k0 = indexes_k0b3z0
        indexes_k1 = indexes_k1b3z1
    elif nd == 4:
        indexes_k0 = indexes_k0b4z0
        indexes_k1 = indexes_k1b4z1
    else: raise ValueError

    for i, (cp, key) in enumerate(zip(checkpoints, reference_keys)):
        print(f"Dataset {i+1}")
        config.path_to_checkpoints = f"outputs/{cp}"
        k0ref = key & 0xffffffffffffffff
        k1ref = (key >> 64) & 0xffffffffffffffff
        k1ref = k1ref ^ 0xf0 ^ k0ref

        total, count = success_rates(config, "k0", "z0", indexes_k0, nd, k0ref, nbtrace_range)
        print(f"Recover k0, d={nd}, total runs ({total:3d}):")
        print(f"Success count:")
        print(f"t{i}_k0b{nd} = {count}")

        total, count = success_rates(config, "k1", "z1", indexes_k1, nd, k1ref, nbtrace_range)
        print(f"Recover k1, d={nd}, total runs ({total:3d}):")
        print(f"Success count:")
        print(f"t{i}_k1b{nd} = {count}")
        print()
    
    print("Check out the precomputed results in the file 'visualize.py'!")

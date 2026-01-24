import os
import pickle
import argparse
import numpy as np
import matplotlib.pyplot as plt
from heapq import heapreplace, heappush
from queue import PriorityQueue

indexes_k0b1z0 = [1, 2, 5, 8, 11, 12, 15, 18, 19, 22, 25, 28, 29, 32, 35, 39, 42, 45, 49, 52, 55, 59, 62]     # 23
indexes_k1b1z1 = [3, 5, 6, 7, 13, 15, 17, 22, 24, 26, 32, 33, 34, 39, 41, 43, 45, 50, 51, 52, 53, 58, 60, 62] # 24

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

def bytes_to_u64(v: list):
    n = (v[0] << 56) |\
        (v[1] << 48) |\
        (v[2] << 40) |\
        (v[3] << 32) |\
        (v[4] << 24) |\
        (v[5] << 16) |\
        (v[6] <<  8) |\
        (v[7]      )
    return int(n)

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
        # print(f"{j:2d}: {subkey}")

    successrates = [0] * len(nbtrace_range)
    count = 0

    path_prefix = f"{config.path_to_checkpoints}/{target_key}/{selection_function}/b{nd}"
    for idx in indexes:
        for rep in os.listdir(f"{path_prefix}/{idx:02d}"):
            if ".DS_Store" in rep: continue
            path_to_rep = f"{path_prefix}/{idx:02d}/{rep}"

            for i, nbtr in enumerate(nbtrace_range):
                path_to_file = f"{path_to_rep}/{nbtr:07d}.pkl"
                if not os.path.exists(path_to_file):
                    print(path_to_file)
                    raise FileNotFoundError
                with open(path_to_file, "rb") as f: cp = pickle.load(f)
                rho = np.abs(cp["rho"])

                best_guesses = np.argmax(rho.max(1).reshape((1<<(3*nd),)))                
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
                        default="outputs/checkpoints",
                        type=str)
    parser.add_argument("--n-traces",
                        dest="nn",
                        help="Number of traces",
                        default=450000,
                        type=int)
    parser.add_argument("--n-bits-selection-function",
                        dest="nd",
                        help="Number of bits for the selection function",
                        type=int,
                        default=1)
    parser.add_argument("--step",
                        dest="ns",
                        help="Number of traces for each process",
                        default=25000,
                        type=int)
    
    
    config = parser.parse_args()

    nn = config.nn
    ns = config.ns
    nd = config.nd
    nbtrace_range = list(range(ns, nn+1, ns))

    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    k0ref = bytes_to_u64(key[:8])
    k1ref = bytes_to_u64(key[8:])
    k1ref = k1ref ^ 0xf0 ^ k0ref

    t0, ssk0 = success_rates(config, "k0", "z0", indexes_k0b1z0, nd, k0ref, nbtrace_range)
    print(f"Recover k0, d={nd}, total runs ({t0:3d}):")
    print(f"Success count:")
    print(f"{ssk0}")

    t1, ssk1 = success_rates(config, "k1", "z1", indexes_k1b1z1, nd, k1ref, nbtrace_range)
    print(f"Recover k1, d={nd}, total runs ({t1:3d}):")
    print(f"Success count:")
    print(f"{ssk1}")
    print()
    
    # print("Check out the precomputed results in the file 'visualize.py'!")
    nbtrace_range = list(range(ns, nn+1, ns))
    plt.figure(figsize=(6, 4))

    srk0 = (np.array(ssk0)/t0)**t0
    srk1 = (np.array(ssk1)/t1)**t1
    fullsr = srk0*srk1

    plt.xlabel("Number of traces")
    plt.ylabel("Success rate (%)")
    plt.xlim([0, 450000])
    plt.ylim([0, 105])
                
    plt.plot(nbtrace_range, srk0*100, "--", color="orange", label=r"Recover 3 bits of $k_0$")
    plt.plot(nbtrace_range, srk1*100, "--", color="red", label=r"Recover 3 bits of $k_1$")
    plt.plot(nbtrace_range, fullsr*100, color="blue", label="Recover full 128-bit key")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/sr.png")
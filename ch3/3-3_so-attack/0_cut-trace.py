import numpy as np
import argparse
from matplotlib import pyplot as plt

# Cut the trace by minimizing the variance
def cut(trace, nb_blocks, hint=None):
    nb_samples = np.shape(trace)[0]
    min_variance = np.inf

    if not hint:
        block_size_range = range(int(nb_samples / (1.25 * nb_blocks)),
                                int(nb_samples / (0.75 * nb_blocks)))
    else:
        block_size_range = range(hint - 50, hint + 50)
            
    for block_size in block_size_range:
        for begin_offset in range(0, nb_samples):
            if begin_offset + nb_blocks * block_size > nb_samples:
                continue
            cut_trace = trace[begin_offset:begin_offset + nb_blocks * block_size]
            reshaped_trace = np.reshape(cut_trace, (nb_blocks, -1))
            variance = np.mean(np.var(reshaped_trace, axis=0))
            if variance < min_variance:
                min_variance = variance
                result = (block_size, begin_offset)

    block_size, begin_offset = result
    print(f"Block size  : {block_size}")
    print(f"Begin offset: {begin_offset}")

    reshaped_trace = np.reshape(trace[begin_offset:begin_offset + nb_blocks * block_size], (nb_blocks, -1))
    plt.title("Overlapped")
    plt.plot(reshaped_trace.T)
    plt.savefig("outputs/overlapped.png")

    # plt.plot(trace)
    # for sep in [begin_offset + block_size * i for i in range(nb_blocks + 1)]:
    #     plt.vlines(sep, np.min(trace), np.max(trace), "red")
    # plt.show()
    return begin_offset, block_size 

if __name__ == "__main__":
    print(f"[Figure 3.5, page 36]")   
    print(f"Cut the trace to get the interval for our targeted first round.")
    print(f"It takes ~1 minutes.")

    parser = argparse.ArgumentParser()
    parser.add_argument("--path-to-trace",
                        dest="path_to_trace",
                        help="Path to trace.",
                        type=str,
                        required=True)
    parser.add_argument("--nb-blocks",
                        dest="nb_blocks",
                        help="Number of rounds (blocks). In our case, it is 12.",
                        type=int,
                        default=12)
    parser.add_argument("--hint",
                        dest="hint",
                        help="Hint for the block size",
                        type=int,
                        default=1424)

    config = parser.parse_args()

    path_to_trace = config.path_to_trace
    nb_blocks     = config.nb_blocks
    hint          = config.hint
    
    trace = np.load(path_to_trace)

    # Calculate the variance and cut the trace
    begin_offset, block_size = cut(trace, nb_blocks, hint)

    # # Result after running the above function
    # begin_offset = 141
    # block_size = 1400

    plt.figure(figsize=(10, 4))
    plt.plot(trace[:17500])
    for sep in [begin_offset + block_size * i for i in range(nb_blocks + 1)]:
        plt.vlines(sep, np.min(trace), np.max(trace), "red")

    plt.xlabel("Sample")
    plt.ylabel("Power consumption")
    plt.tight_layout()
    plt.savefig("outputs/ascon-initialization.png")

    plt.figure(figsize=(10, 4))
    plt.plot(trace[begin_offset:begin_offset+block_size])
    plt.xlabel("Sample")
    plt.ylabel("Power consumption")
    plt.tight_layout()
    plt.savefig("outputs/first-round.png")

    print("Check the figures `overlapped.png`, `ascon-initialization.png`, and `first-round.png` in the folder `outputs`")
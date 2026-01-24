# Experiment: [Second-Order Attack] 
[2 human-minutes + 10 compute-hours + 8GB disk]

This folder contains the artifact used to validate the claims in Section 3.4 of the manuscript. 

## Main idea

We perform a second-order CPA attack on a masked implementation of Ascon-AEAD. Our goal is to verify our analysis on the selection function and provide the first practical indication of the data and computational cost for full key recovery in a protected implementation.

```text
3-4_so-attack
├── incremental-cpa    : incremental second-order cpa
├── save-checkpoint    : logs of attack outputs
├── 0_cut-trace.py     : analysis script
├── 2_sopeak.py        : analysis script
├── 3_soctdep.py       : analysis script
├── 4_successcount.py  : analysis script
├── run-attack.sh      : automation script
├── run-preprocess.sh  : automation script
├── run-postprocess.sh : automation script
└── README.md
```

The main steps of this experiment are as follows:
- We identify a smaller trace interval to target in order to reduce the computational cost. 
- We perform the incremental CPA attack and log the results for multiple numbers of traces.
- We compute the success rates and visualize the attack outputs.

## Execution

Run the following automation script for preprocessing:
```sh
./run-preprocess.sh
```

Run the following automation script for key recovery [~10 compute-hours]:
```sh
./run-attack.sh
```

Run the following automation script for success rates and visualization:
```sh
./run-postprocess.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Figure 3.7, page 39]
- [Figure 3.8, page 39]
- [Figure 3.9, page 40]

## Reusability

The second-order CPA is implemented in an incremental manner and is therefore very memory-efficient. It is configurable through parameters such as the total number of traces, the number of traces processed per step, trace intervals, the indexes of targeted key bits, the window size, etc. 

I strongly believe that this implementation can also be reused for CPA attacks against other algorithms. It only require a minimal change for the selection function, which is algorithm-dependent.

```
python3.10 incremental-cpa/main.py --task 1\
                 --selection-function z0\
                 --n-bits-selection-function 1\
                 --target-key k0\
                 --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                 --n-rank 8\
                 --n-traces 400000\
                 --n-repetition 1\
                 --space 400000\
                 --path-to-traces ../data/protected/traces\
                 --start-sample 1050\
                 --end-sample 1400\
                 --step 25000\
                 --window 50\
                 --data-type float64\
                 --path-to-nonces ../data/protected/nonces.npy\
                 --path-to-checkpoints outputs/checkpoints
```
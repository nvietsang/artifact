# Experiment: [Number of CPA runs by SAT solver] 
[2 human-minutes + 1 compute-minute + 20KB disk]

This folder contains the artifact used to validate the claims in Section 3.3 of the manuscript. 

## Main idea

To recover the full 128-bit key of Ascon-AEAD, multiple CPA runs are required, since a single CPA run recovers only 3 key bits. We determine the optimal number of CPA runs to minimize the effort for full key recovery. We show that this problem can be formalized as a set cover problem and solved using a SAT solver.

```text
3-3_cpa-runs
├── nbtuples.py : SAT solver  
├── run.sh      : automation script
└── README.md
```

## Execution

Run the following automation script:
```sh
./run.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Table 3.6, page 35]
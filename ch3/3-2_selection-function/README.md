# Experiment: [Analysis of Selection Function]
[2 human-minutes + 1 compute-minute + 1MB disk]

This folder contains the artifact used to validate the claims in Section 3.2 of the manuscript. 

## Main idea

We provide a comprehensive analysis of the selection functions used in the literature. We experimentally show that different choices of the selection function can determine the success or failure of CPA attacks on Ascon-AEAD.

```text
3-2_selection-function
├── 0_distribution.py   : analysis script
├── 1_pure-y0.py        : analysis script
├── 2_finetuned-z0.py   : analysis script
├── 3_finetuned-y0.py   : analysis script
├── run.sh              : automation script
└── README.md
```

The main steps of this experiment are as follows:
- For each choice of selection function, we calculate the distribution vectors of the intermediate value for every key candidate, and the Pearson's correlation coefficients between these vectors.
- We perform the CPA attack with the traces recorded from the execution of the reference Ascon-AEAD, using different selection functions.
- We visualize the attack outputs to verify the effectiveness of each choice for the selection function.

## Execution

Run the following automation script:
```sh
./run.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Table 3.1, page 25]
- [Table 3.2, page 26]
- [Table 3.3, page 28]
- [Table 3.4, page 30]
- [Table 3.5, page 30]
- [Figure 3.1, page 27]
- [Figure 3.3, page 31]
- [Figure 3.4, page 32]
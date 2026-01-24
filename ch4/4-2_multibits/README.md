# Experiment: [Multi-bit Selection Functions]
[2 human-minutes + 2 compute-hours + 15GB disk]

This folder contains the artifact used to validate the claims in Section 4.2 of the manuscript. 

## Main idea

We run the incremental CPA with different number of bits for the selection function (a core factor of CPA attacks). This number is a parameter, denoted by $d$. We validate that when $d=2$, $d=3$, and $d=4$, the success rates are higher than when $d=1$.

```text
4-2_multibits
├── incpa-d        : incremental CPA with parameter d
├── run-nbtuples   : find minimum number of CPA runs
├── run-incpad1.sh : run CPA with d=1
├── run-incpad2.sh : run CPA with d=2
├── run-incpad3.sh : run CPA with d=3
├── run-incpad4.sh : run CPA with d=4
├── run-countd1.sh : measure success rates for d=1
├── run-countd2.sh : measure success rates for d=2
├── run-countd3.sh : measure success rates for d=3
├── run-countd4.sh : measure success rates for d=4
├── successcount.py
├── run-visualization.sh
├── visualize.py
└── README.md
```

The main steps of this experiment are as follows:
- First, we find the minimum number of CPA runs for each parameter $d=1,2,3,4$.
- Next, we run the incremental CPA for each parameter $d=1,2,3,4$ on the downloaded datasets.
- Then, we calculate the success rates with increasing number of traces for each of $d=1,2,3,4$.
- Finally, we visualize the results.

## Minimum number of CPA runs

Find the minimum number of CPA runs for each parameter $d=1,2,3,4$ by SAT solver:
```sh
./run-nbtuples.sh
```

## Execution

We sequentially run the CPA for each parameter $d=1,2,3,4$ on 5 different datasets. During these runs, the log files are written to the `outputs` folder, which will be used later to compute the success rates.

### $d=1$
Run the incremental CPA for $d=1$ [~15 compute-minutes]:
```sh
./run-incpad1.sh
```
Calculate the success rates with an increasing number of traces for $d=1$:
```sh
./run-countd1.sh
```

### $d=2$
Run the incremental CPA for $d=2$ [~50 compute-minutes]:
```sh
./run-incpad2.sh
```
Calculate the success rates with an increasing number of traces for $d=2$:
```sh
./run-countd2.sh
```

### $d=3$ and $d=4$
For $d=3$ and $d=4$, running the following scripts is *NOT recommended*, as it requires a long execution time, especially for $d = 4$. In my experiments, I completed these tasks using parallel key recovery on the university’s computing cluster [Table 4.5, page 51]. The results of these tasks are already included in the calculation of the success rates.

Run the incremental CPA for $d=3$ [~13.5 compute-hours]:
```sh
./run-incpad3.sh
```
Calculate the success rates with an increasing number of traces for $d=3$:
```sh
./run-countd3.sh
```

Run the incremental CPA for $d=4$ [~173.5 compute-hours]:
```sh
./run-incpad4.sh
```
Calculate the success rates with an increasing number of traces for $d=4$:
```sh
./run-countd4.sh
```

### Visualization

Plot the success rates for $d=1,2,3,4$:
```sh
./run-visualization.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Table 4.4, page 49]
- [Table 4.6, page 55]
- [Figure 4.2, page 50]

## Reusability

The Correlation Power Analysis (CPA) is implemented in an incremental manner and is therefore very memory-efficient. It is configurable through parameters such as the total number of traces, the number of traces processed per step, trace intervals, the number of bits for the selection function (parameter $d$), etc. 

I strongly believe that this implementation can also be reused for CPA attacks against other algorithms. It only require a minimal change for the selection function, which is algorithm-dependent.

```
time python3 main.py --task 0\
                     --selection-function z4\
                     --n-bits-selection-function 1\
                     --target-key k0\
                     --first-subkey-index 1 6 7 9 11 12 17 22 23 25 27 28 33 34 38 39 43 44 48 49 54 55 59 60\
                     --n-rank 8\
                     --n-traces 10000\
                     --n-repetition 3\
                     --space 10000\
                     --path-to-traces ../bi32-armv6/traces\
                     --start-sample 150\
                     --end-sample 500\
                     --step 200\
                     --data-type float64\
                     --path-to-nonces ../bi32-armv6/nonces.npy\
                     --path-to-checkpoints ../bi32-armv6/checkpoints\
```
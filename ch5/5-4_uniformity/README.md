# Experiment: [Uniformity of Intermediate Value]
[2 human-minutes + 4 compute-minutes + 33MB disk]

This folder contains the artifact used to validate the claims in Section 5.4 of the manuscript. 

## Main idea

We simulate an instruction-skip fault in Ascon-AEAD and compute the probability that the fault is `ineffective` (the output is still correct). The goal is to show that this probability converges to a uniform distribution. This supports our finding that SIFA attacks can be compromised because the intermediate value remains uniformly distributed.

NOTE: We use a simulation rather than a real-hardware experiment, as this guarantees that the targeted instruction is indeed skipped.

```text
5-3_ineffective-proba
├── nonces          : acquisition for common set of nonces
├── ascon.py        : modified implementation of Ascon-AEAD
├── convergence.py  : probability computation
├── README.md
└── run.sh          : automation script
```

The main steps of this experiment are as follows:
- First, we compute the probability that a fault is ineffective with an increasing number of data.
- Next, we visualize the convergence of this probability.

## Preparation

A prerequisite is to run experiment in [../5-3_ineffective-proba/](../5-3_ineffective-proba/) beforehand, as this experiment reuses the previous results.

## Execution

Run the following script:

```sh
./run.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Figure 5.3, page 72]

## References

The implementation of Ascon-AEAD is based on the reference code available at: [https://github.com/meichlseder/pyascon](https://github.com/meichlseder/pyascon)
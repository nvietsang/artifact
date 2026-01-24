# Experiment: [Empirical Probability of Ineffective Faults]
[2 human-minutes + 4 compute-minutes + 250MB disk]

This folder contains the artifact used to validate the claims in Section 5.3 of the manuscript. 

## Main idea

We simulate an instruction-skip fault in Ascon-AEAD and compute the probability that the fault is `ineffective` (the output is still correct). The goal is to show that this probability follows our model.

NOTE: We use a simulation rather than a real-hardware experiment, as this guarantees that the targeted instruction is indeed skipped.

```text
5-3_ineffective-proba
├── faultedAND1 : implementation with a skipped AND (scenario 1)
├── faultedAND2 : implementation with a skipped AND (scenario 2)
├── faultedNOT1 : implementation with a skipped NOT (scenario 1)
├── faultedNOT2 : implementation with a skipped NOT (scenario 2)
├── faultedXOR1 : implementation with a skipped XOR (scenario 1)
├── faultedXOR2 : implementation with a skipped XOR (scenario 2)
├── reference   : reference implementation
├── proba.py
├── README.md
└── run.sh      : automation script
```

The skipped instruction can be found in the file `round.h` in each `faulted*` folder.

The main steps of this experiment are as follows:
- First, we run the reference implementation on a set of inputs and collect the corresponding outputs.
- Next, we run the implementations with a skipped instruction using the same inputs and collect the resulting outputs. 
- Finally, we compare the faulty outputs with reference outputs to identify ineffective faults.

## Execution

Run the following script:

```sh
./run.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Table 5.4, page 67]

## References

The implementation of Ascon-AEAD is based on the reference code available at: [https://github.com/ascon/ascon-c](https://github.com/ascon/ascon-c)
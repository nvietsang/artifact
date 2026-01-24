# Experiment: [Cautionary Notes]
[2 human-minutes + 1 compute-minute + 50MB disk]

This folder contains the artifact used to validate the claims in Section 4.3 of the manuscript. 

## Main idea

In CPA attacks with multi-bit selection functions ($d=2,3,4$), partial correlations exist among the distributions of different key candidates, which may affect the success rates. We run this experiment to substantiate this cautionary observation.

```text
4-3_notes
├── checkpoints : logs of attack outputs at many numbers of traces
├── partialcorrelation.py : analysis of partial correlation
├── run.sh                : automation script
├── visualization.py
└── README.md
```

The main steps of this experiment are as follows:
- First, we compute the distributions of the selection function for all possible key candidates. 
- Then, we examine the Pearson's correlation coefficient between distributions of every key pair.
- Finally, we verify that the success rates can be affected by partial correlations between the distributions of key candidates. This verification uses the previously computed logs of attack outputs.

## Execution

Run the following automation script:
```sh
./run
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Figure 4.4, page 54]
- [Figure 4.5, page 54]
- [Table 4.6, page 55]
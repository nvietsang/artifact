# Artifacts for chapter 3

This folder contains the artifacts supporting the claims in Section 3.2, Section 3.3, and 3.4 of the manuscript.

```
ch3
├── 3-2_selection-function
├── 3-3_cpa-runs
├── 3-4_so-attack
├── data
└── README.md
```

## Preparation

A prerequisite is that trace datasets (5.3GB when unzipped) must be downloaded via the following link: [https://drive.google.com/file/d/1GrMBoAgeESW0OQo8ChJyMxWoDAlnOaHj/view?usp=share_link](https://drive.google.com/file/d/1GrMBoAgeESW0OQo8ChJyMxWoDAlnOaHj/view?usp=share_link)

Make sure that the downloaded file is unzipped and placed in this folder. The following directory must exist:
```
artifact/ch3/data
```

The process of downloading and unzipping takes about 10 minutes.

The dataset contains 500,000 traces acquired from a protected implementation for a second-order attack, and 10,000 traces acquired from the reference implementation for our analyses.

## Experiments

There are three experiments with IDs (E3.1), (E3.2), and (E3.3) in this folder.

### [Analysis of Selection Function]
[2 human-minutes + 1 compute-minute + 1MB disk]

Go to [3-2_selection-function](./3-2_selection-function/) and follow the README there.

```sh
cd 3-2_selection-function
```

### [Number of CPA runs by SAT solver] 
[2 human-minutes + 1 compute-minute + 20KB disk]

Go to [3-3_cpa-runs](./3-3_cpa-runs/) and follow the README there.

```sh
cd 3-3_cpa-runs
```

### [Second-Order Attack] 
[2 human-minutes + 10 compute-hours + 8GB disk]

Go to [3-4_so-attack](./3-4_so-attack/) and follow the README there.

```sh
cd 3-4_so-attack
```
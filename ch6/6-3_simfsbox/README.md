# Simulation: [Simulation of PFA with faulted Sbox]
[2 human-minutes + 1 compute-minute + 1MB disk]

This folder contains the artifact used to validate the claims in Section 6.3 of the manuscript. 

## Main idea

We simulate an instruction-skip fault in S-box generation of AES and recover the full 128-bit key by a statistical analysis. The goal is to validate the attack path presented in the manuscript.

```text
6-3_simfsbox
├── faultingsbox    : faulted AES from MbedTLS
├── keyrecovery.py  : key recovery
├── visualize.py    : visualization for results
├── README.md
└── run.sh          : automation script
```

The skipped instruction can be found in the file `main.c` in the `faultingsbox` folder.

The main steps of this simulation are as follows:
- First, we randomly skip an instruction in the S-box generation and collect a number of ciphertexts.
- Next, we recover the key from the faulted ciphertexts.
- Finally, we visualize the results.

## Execution

Run the following script:

```sh
./run.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Automated attack, page 83]
- [Figure 6.1, page 82]

## References

The implementation of AES is extracted from the MbedTLS library: [https://github.com/Mbed-TLS/mbedtls](https://github.com/Mbed-TLS/mbedtls)

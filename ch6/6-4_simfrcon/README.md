# Simulation: [Simulation of PFA with faulted Rcon]
[2 human-minutes + 1 compute-minute + 1MB disk]

This folder contains the artifact used to validate the claims in Section 6.4 of the manuscript. 

## Main idea

We simulate an instruction-skip fault in the generation of round constants (Rcon) of AES and recover the full 128-bit key by a differential analysis. The goal is to validate the attack path presented in the manuscript.

```text
6-4_simfrcon
├── reference       : reference AES from MbedTLS
├── faultingrcon    : faulted AES
├── keyrecovery.py  : key recovery
├── README.md
└── run.sh          : automation script
```

The skipped instruction can be found in the file `main.c` in the `faultingrcon` folder.

The main steps of this simulation are as follows:
- First, we run the reference implementation and collect 3 correct ciphertexts.
- Next, we run the faulted implementation (in which the instruction of generating the 8-th round constant is skipped) and collect 3 faulty ciphertexts.
- Finally, we recover the key from the 3 correct-faulty ciphertext pairs.

## Execution

Run the following script:

```sh
./run.sh
```

## Results

The results will be written to the folder [outputs](./outputs/)

This experiment is to validate the following items in the manuscript:
- [Attack path, page 87]

## References

The implementation of AES is extracted from the MbedTLS library: [https://github.com/Mbed-TLS/mbedtls](https://github.com/Mbed-TLS/mbedtls)

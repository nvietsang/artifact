# Experiment: [Experiment of PFA with faulted Rcon]
[2 human-minutes + 10 compute-minute + 33MB disk]

This folder contains the artifact used to validate the claims in Section 6.4 of the manuscript. 

NOTE: This experiment requires a ChipWhisperer Lite integrated with a 32-bit STM32F303 target. Other ChipWhisperer platforms or alternative fault injection equipment, but these have not been tested or prepared in this artifact.

It requires to install the `chipwhisperer` package:
```sh
pip3 install chipwhisperer==6.0.6
```

## Main idea

We inject an instruction-skip fault by a clock glitch in the generation of round constants (Rcon) of AES and recover the full 128-bit key by a differential analysis. The goal is to validate the attack path presented in the manuscript.

```text
6-4_expfrcon
├── hal                 : config of CW platform
├── simpleserial        : config of CW platform
├── Makefile.inc        : config of CW platform
├── simpleserial-glitch : C-implementation of AES (deployed to CW)
├── plts.txt            : 3 plaintexts
├── ccpts.txt           : 3 correct ciphertexts
├── keyrecovery.py      : key recovery
├── README.md
└── run.py              : script for interaction with CW
```

The main steps of this simulation are as follows:
- We assume that we already have 3 plaintexts and 3 corresponding correct ciphertexts.
- We inject a clock glitch to skip an instruction in the generation of the 8-th round constant, then collect 3 faulty ciphertexts.
- Finally, we recover the key from the 3 correct-faulty ciphertext pairs.

## Execution

Compile the source code:
```sh
cd simpleserial-glitch && make -j && ..
```

Insert clock glitch and collect ciphertexts
```sh
python3 run.py
```
This script does the following tasks:

- Transfer the binary code to the target
- Request the first encryption, before which the round constants are generated
- Request 3 ciphertexts, then verify whether the expected fault has occurred
    - If yes, recover the key 
    - If no, reset and try with different glitch parameter



## Results

This experiment is to validate the following items in the manuscript:
- [Attack path, page 87]

## References

The implementation of AES is extracted from the MbedTLS library: [https://github.com/Mbed-TLS/mbedtls](https://github.com/Mbed-TLS/mbedtls)

The setup of ChipWhisperer platform is from [https://github.com/newaetech/chipwhisperer](https://github.com/newaetech/chipwhisperer)

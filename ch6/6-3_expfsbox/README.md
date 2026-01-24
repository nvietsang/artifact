# Experiment: [Experiment of PFA with faulted Sbox]
[2 human-minutes + 10 compute-minute + 33MB disk]

This folder contains the artifact used to validate the claims in Section 6.3 of the manuscript. 

NOTE: This experiment requires a ChipWhisperer Lite integrated with a 32-bit STM32F303 target. Other ChipWhisperer platforms or alternative fault injection equipment, but these have not been tested or prepared in this artifact.

It requires to install the `chipwhisperer` package:
```sh
pip3 install chipwhisperer==6.0.6
```

## Main idea

We inject an instruction-skip fault by a clock glitch in the S-box generation of AES and recover the full 128-bit key by a statistical analysis. The goal is to validate the attack path presented in the manuscript.

```text
6-3_expfsbox
├── hal                 : config of CW platform
├── simpleserial        : config of CW platform
├── Makefile.inc        : config of CW platform
├── simpleserial-glitch : C-implementation of AES (deployed to CW)
├── keyrecovery.py      : key recovery
├── README.md
├── keyrecovery.py      : visualization
└── run.py              : script for interaction with CW
```

The main steps of this experiment are as follows:
- First, we inject a glitch to skip an instruction in the S-box generation and collect a number of ciphertexts.
- Next, we recover the key from the faulted ciphertexts.
- Finally, we visualize the results.

## Execution

Compile the source code:
```sh
cd simpleserial-glitch && make -j && ..
```

Insert clock glitch and collect ciphertexts:
```sh
python3 run.py
```

Analyze ciphertexts:
```sh
python3 visualize.py
```

Key recovery
```sh
python3 keyrecovery.py
```

## Results

This experiment is to validate the following items in the manuscript:
- [Automated attack, page 83]
- [Figure 6.1, page 82]

## References

The implementation of AES is extracted from the MbedTLS library: [https://github.com/Mbed-TLS/mbedtls](https://github.com/Mbed-TLS/mbedtls)

The setup of ChipWhisperer platform is from [https://github.com/newaetech/chipwhisperer](https://github.com/newaetech/chipwhisperer)
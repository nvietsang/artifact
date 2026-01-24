# Artifacts for PhD thesis: Physical Attacks against Symmetric Cryptography Standards

My artifacts are organized into four main parts, corresponding to the four main chapters of the thesis’s contributions. These are represented by the folders [ch3](./ch3/), [ch4](./ch4/), [ch5](./ch5/), and [ch6](./ch6/) (for chapters 3, 4, 5, and 6 in the manuscript).

For a smooth evaluation and to optimize the required time, I highly recommend the following evaluation order: [ch5](./ch5/) $\to$ [ch6](./ch6/) $\to$ [ch3](./ch3/) $\to$ [ch4](./ch4/).

In each directory, there is a README file providing instructions for running the artifacts.

```text
.
├── ch3
├── ch4
├── ch5
├── ch6
├── .gitignore
├── basictest.sh
├── Dockerfile
├── LICENSE
└── README.md
```

## Set-up

My artifacts require to create a Docker image to run Python scripts and C code. All required software packages with appropriate versions are configured in the `Dockerfile`.

Create the docker image:
```sh
docker build -t artifact .
```

Run the image with volume mount:
```sh
docker run -it -v $(pwd):/app artifact
```

## Basic test

Run the following test:
```sh
./basictest.sh
```

The expected output is:
```text
Python 3.10.19
NumPy version: 2.2.6
matplotlib version: 3.10.3
pycryptosat version: 5.11.21
tqdm version: 4.67.1
```
#!/bin/bash

# Check if Python is installed
if ! command -v python3.10 &> /dev/null
then
    echo "Python is not installed."
    exit 1
fi

# Print Python version
python3 --version

# Check if NumPy is installed
if python3 -c "import numpy" &> /dev/null; then
    python3 -c "import numpy; print(f'NumPy version: {numpy.__version__}')"
else
    echo "NumPy is not installed."
fi

# Check if matplotlib is installed
if python3 -c "import matplotlib" &> /dev/null; then
    python3 -c "import matplotlib; print(f'matplotlib version: {matplotlib.__version__}')"
else
    echo "matplotlib is not installed."
fi

# Check if pycryptosat is installed
if python3 -c "import pycryptosat" &> /dev/null; then
    python3 -c "import pycryptosat; print(f'pycryptosat version: {pycryptosat.__version__}')"
else
    echo "pycryptosat is not installed."
fi

# Check if tqdm is installed
if python3 -c "import tqdm" &> /dev/null; then
    python3 -c "import tqdm; print(f'tqdm version: {tqdm.__version__}')"
else
    echo "tqdm is not installed."
fi

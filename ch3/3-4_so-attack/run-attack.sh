mkdir -p outputs/checkpoints

if [ ! -d "../data/protected" ]; then
    echo "Error: ../data/protected does not exist"
    exit 1
fi

python3 incremental-cpa/main.py --task 1\
                 --selection-function z0\
                 --n-bits-selection-function 1\
                 --target-key k0\
                 --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                 --n-rank 8\
                 --n-traces 450000\
                 --n-repetition 1\
                 --space 450000\
                 --path-to-traces ../data/protected/traces\
                 --start-sample 1050\
                 --end-sample 1400\
                 --step 25000\
                 --window 50\
                 --data-type float64\
                 --path-to-nonces ../data/protected/nonces.npy\
                 --path-to-checkpoints outputs/checkpoints

python3 incremental-cpa/main.py --task 1\
                 --selection-function z1\
                 --n-bits-selection-function 1\
                 --target-key k1\
                 --first-subkey-index 3 5 6 7 13 15 17 22 24 26 32 33 34 39 41 43 45 50 51 52 53 58 60 62\
                 --n-rank 8\
                 --n-traces 450000\
                 --n-repetition 1\
                 --space 450000\
                 --path-to-traces ../data/protected/traces\
                 --start-sample 1050\
                 --end-sample 1400\
                 --step 25000\
                 --window 50\
                 --data-type float64\
                 --path-to-nonces ../data/protected/nonces.npy\
                 --path-to-checkpoints outputs/checkpoints

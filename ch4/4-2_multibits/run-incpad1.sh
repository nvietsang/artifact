mkdir -p outputs

cd incpa-d

echo "Running incremental CPA on 5 different datasets for parameters:"
echo "d = 1 (1-bit selection function)"

echo
echo "Recovering k0 on dataset 1"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 1\
                   --target-key k0\
                   --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                   --n-rank 3\
                   --n-traces 10000\
                   --n-repetition 1\
                   --space 10000\
                   --path-to-traces ../../data/traces0\
                   --start-sample 0\
                   --end-sample 1000\
                   --step 250\
                   --data-type float64\
                   --path-to-nonces ../../data/nonces0.npy\
                   --path-to-checkpoints ../outputs/checkpoints0 > /dev/null 2>&1
echo "Recovering k1 on dataset 1"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 1\
                     --target-key k1\
                     --first-subkey-index 3 5 6 7 13 15 17 22 24 26 32 33 34 39 41 43 45 50 51 52 53 58 60 62\
                     --n-rank 8\
                     --n-traces 10000\
                     --n-repetition 1\
                     --space 10000\
                     --path-to-traces ../../data/traces0\
                     --start-sample 0\
                     --end-sample 1000\
                     --step 250\
                     --data-type float64\
                     --path-to-nonces ../../data/nonces0.npy\
                     --path-to-checkpoints ../outputs/checkpoints0 > /dev/null 2>&1
echo "Done! The logs are written to 'checkpoints0' in the folder 'outputs'."

echo
echo "Recovering k0 on dataset 2"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 1\
                   --target-key k0\
                   --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                   --n-rank 3\
                   --n-traces 10000\
                   --n-repetition 1\
                   --space 10000\
                   --path-to-traces ../../data/traces1\
                   --start-sample 0\
                   --end-sample 1000\
                   --step 250\
                   --data-type float64\
                   --path-to-nonces ../../data/nonces1.npy\
                   --path-to-checkpoints ../outputs/checkpoints1 > /dev/null 2>&1
echo "Recovering k1 on dataset 2"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 1\
                     --target-key k1\
                     --first-subkey-index 3 5 6 7 13 15 17 22 24 26 32 33 34 39 41 43 45 50 51 52 53 58 60 62\
                     --n-rank 8\
                     --n-traces 10000\
                     --n-repetition 1\
                     --space 10000\
                     --path-to-traces ../../data/traces1\
                     --start-sample 0\
                     --end-sample 1000\
                     --step 250\
                     --data-type float64\
                     --path-to-nonces ../../data/nonces1.npy\
                     --path-to-checkpoints ../outputs/checkpoints1 > /dev/null 2>&1
echo "Done! The logs are written to 'checkpoints1' in the folder 'outputs'."

echo
echo "Recovering k0 on dataset 3"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 1\
                   --target-key k0\
                   --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                   --n-rank 3\
                   --n-traces 10000\
                   --n-repetition 1\
                   --space 10000\
                   --path-to-traces ../../data/traces2\
                   --start-sample 0\
                   --end-sample 1000\
                   --step 250\
                   --data-type float64\
                   --path-to-nonces ../../data/nonces2.npy\
                   --path-to-checkpoints ../outputs/checkpoints2 > /dev/null 2>&1
echo "Recovering k1 on dataset 3"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 1\
                     --target-key k1\
                     --first-subkey-index 3 5 6 7 13 15 17 22 24 26 32 33 34 39 41 43 45 50 51 52 53 58 60 62\
                     --n-rank 8\
                     --n-traces 10000\
                     --n-repetition 1\
                     --space 10000\
                     --path-to-traces ../../data/traces2\
                     --start-sample 0\
                     --end-sample 1000\
                     --step 250\
                     --data-type float64\
                     --path-to-nonces ../../data/nonces2.npy\
                     --path-to-checkpoints ../outputs/checkpoints2 > /dev/null 2>&1
echo "Done! The logs are written to 'checkpoints2' in the folder 'outputs'."

echo
echo "Recovering k0 on dataset 4"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 1\
                   --target-key k0\
                   --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                   --n-rank 3\
                   --n-traces 10000\
                   --n-repetition 1\
                   --space 10000\
                   --path-to-traces ../../data/traces3\
                   --start-sample 0\
                   --end-sample 1000\
                   --step 250\
                   --data-type float64\
                   --path-to-nonces ../../data/nonces3.npy\
                   --path-to-checkpoints ../outputs/checkpoints3 > /dev/null 2>&1
echo "Recovering k1 on dataset 4"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 1\
                     --target-key k1\
                     --first-subkey-index 3 5 6 7 13 15 17 22 24 26 32 33 34 39 41 43 45 50 51 52 53 58 60 62\
                     --n-rank 8\
                     --n-traces 10000\
                     --n-repetition 1\
                     --space 10000\
                     --path-to-traces ../../data/traces3\
                     --start-sample 0\
                     --end-sample 1000\
                     --step 250\
                     --data-type float64\
                     --path-to-nonces ../../data/nonces3.npy\
                     --path-to-checkpoints ../outputs/checkpoints3 > /dev/null 2>&1
echo "Done! The logs are written to 'checkpoints3' in the folder 'outputs'."

echo
echo "Recovering k0 on dataset 5"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 1\
                   --target-key k0\
                   --first-subkey-index 1 2 5 8 11 12 15 18 19 22 25 28 29 32 35 39 42 45 49 52 55 59 62\
                   --n-rank 3\
                   --n-traces 10000\
                   --n-repetition 1\
                   --space 10000\
                   --path-to-traces ../../data/traces4\
                   --start-sample 0\
                   --end-sample 1000\
                   --step 250\
                   --data-type float64\
                   --path-to-nonces ../../data/nonces4.npy\
                   --path-to-checkpoints ../outputs/checkpoints4 > /dev/null 2>&1
echo "Recovering k1 on dataset 5"
echo "This takes about 3 minutes..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 1\
                     --target-key k1\
                     --first-subkey-index 3 5 6 7 13 15 17 22 24 26 32 33 34 39 41 43 45 50 51 52 53 58 60 62\
                     --n-rank 8\
                     --n-traces 10000\
                     --n-repetition 1\
                     --space 10000\
                     --path-to-traces ../../data/traces4\
                     --start-sample 0\
                     --end-sample 1000\
                     --step 250\
                     --data-type float64\
                     --path-to-nonces ../../data/nonces4.npy\
                     --path-to-checkpoints ../outputs/checkpoints4 > /dev/null 2>&1
echo "Done! The logs are written to 'checkpoints4' in the folder 'outputs'."

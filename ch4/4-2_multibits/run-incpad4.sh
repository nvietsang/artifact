mkdir -p outputs

cd incpa-d

echo "Running incremental CPA on 5 different datasets for parameters:"
echo "d = 4 (4-bit selection function)"

echo
echo "Recovering k0 on dataset 1"
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 4\
                   --target-key k0\
                   --first-subkey-index 28 32 36 40 44 55 59 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 4\
                     --target-key k1\
                     --first-subkey-index 6 16 24 34 42 52 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 4\
                   --target-key k0\
                   --first-subkey-index 28 32 36 40 44 55 59 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 4\
                     --target-key k1\
                     --first-subkey-index 6 16 24 34 42 52 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 4\
                   --target-key k0\
                   --first-subkey-index 28 32 36 40 44 55 59 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 4\
                     --target-key k1\
                     --first-subkey-index 6 16 24 34 42 52 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 4\
                   --target-key k0\
                   --first-subkey-index 28 32 36 40 44 55 59 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 4\
                     --target-key k1\
                     --first-subkey-index 6 16 24 34 42 52 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                   --selection-function z0\
                   --n-bits-selection-function 4\
                   --target-key k0\
                   --first-subkey-index 28 32 36 40 44 55 59 60\
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
echo "This takes about 34.7 hours..."
python3.10 main.py --task 0\
                     --selection-function z1\
                     --n-bits-selection-function 4\
                     --target-key k1\
                     --first-subkey-index 6 16 24 34 42 52 60\
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

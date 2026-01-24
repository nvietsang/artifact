mkdir -p outputs

echo "[Table 3.1, page 25]"
echo "[Table 3.2, page 26]"
echo "[Table 3.3, page 28]"
echo "[Table 3.4, page 30]"
echo "[Table 3.5, page 30]"
echo "Computing distributions and correlations between key candidates..."
python3 0_distribution.py > outputs/0_distribution.txt
echo "Done! Check out the file '0_distribution.txt' in the folder 'outputs'."

if [ ! -d "../data/reference" ]; then
    echo "Error: ../data/reference does not exist"
    exit 1
fi

echo
echo "[Figure 3.1, page 27]"
echo "Visualizing correlation traces when using y_0^j as the intermediate value..."
python3 1_pure-y0.py > /dev/null 2>&1
echo "Done! Check out the figures 'py0_k0k1_**.png' in the folder 'outputs'."

echo 
echo "[Figure 3.3, page 31]"
echo "Visualizing correlation traces for all key candidates when using z_0^j (tilde) as the intermediate value..."
python3 2_finetuned-z0.py > /dev/null 2>&1
echo "Done! Check out the figure 'ftz0k0.png' in the folder 'outputs'."

echo
echo "[Figure 3.4, page 32]"
echo "Visualizing correlation traces when using y_0^j (tilde) as the intermediate value..."
python3 3_finetuned-y0.py > /dev/null 2>&1
echo "Done! Check out the figures 'ftyk0_0.png' and 'ftyk0_1.png' in the folder 'outputs'."

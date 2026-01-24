mkdir -p outputs

cd nonces
make clean
make all
cd ..
# echo "Getting the common set of nonces..."
./nonces/main > outputs/nonces.txt
# echo "Done! Check out the file 'nonces.txt' in the folder 'outputs'"


echo "[Figure 5.3, page 72]"
echo "Verifying the uniformity of intermediate value (a bit)..."
python3 convergence.py
echo "Done! Check out the figure 'convergence.png' in the folder 'outputs'."
echo "Note that the figure may be different from the one in the manuscript because the data is random."
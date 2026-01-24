mkdir -p outputs

echo "Simulating attack with an instruction skip in S-box generation..."
echo "Collecting faulty ciphertexts..."
cd faultingsbox
make
cd ..
./faultingsbox/main > outputs/simfsbox.txt

echo
echo "Recovering the key..."
echo "[Automated attack, page 83]"
python3 keyrecovery.py > outputs/keyrecovery.txt
echo "Done! Check out the files 'simfsbox.txt' and 'keyrecovery.txt' in the folder 'outputs'."

echo
echo "Visualizing the results..."
echo "[Figure 6.1, page 82]"
python3 visualize.py --byte-index 15
echo "Done! Check out the file 'proba.png' in the folder 'outputs'."
echo "Note that the figure may be different from the one in the manuscript because the data is random."
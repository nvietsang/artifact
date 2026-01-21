mkdir -p outputs

echo "Collecting 3 correct ciphertexts..."
cd reference
make
cd ..
./reference/main > outputs/reference.txt
echo "Done! Check out the file 'reference.txt' and 'ccpts.txt' in the folder 'outputs'."

echo
echo "Simulating attack with an instruction skip in round constant generation..."
echo "Collecting 3 faulty ciphertexts..."
cd faultingrcon
make
cd ..
./faultingrcon/main > outputs/faultingrcon.txt
echo "Done! Check out the file 'faultingrcon.txt' and 'fcpts.txt' in the folder 'outputs'."

echo
echo "Recovering the key by differential fault analysis..."
python3.10 keyrecovery.py > outputs/keyrecovery.txt
echo "Done! Check out the file 'keyrecovery.txt' in the folders 'outputs'."
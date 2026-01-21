mkdir -p outputs

# cd reference
# make clean
# make all
# cd ..
# echo "Getting correct outputs from reference implementation..."
# ./reference/main > outputs/coutputs.txt
# echo "Done! Check out the file 'coutputs.txt' in the folder 'outputs'"

# cd faultedAND1
# make clean
# make all
# cd ..
# echo "Simulating AND S1 instruction skip and Getting outputs..."
# ./faultedAND1/main > outputs/foutputs_ANDs1.txt
# echo "Done! Check out the file 'foutputs_ANDs1.txt' in the folder 'outputs'"

# cd faultedAND2
# make clean
# make all
# cd ..
# echo "Simulating AND S2 instruction skip and Getting outputs..."
# ./faultedAND2/main > outputs/foutputs_ANDs2.txt
# echo "Done! Check out the file 'foutputs_ANDs2.txt' in the folder 'outputs'"

# cd faultedNOT1
# make clean
# make all
# cd ..
# echo "Simulating NOT S1 instruction skip and Getting outputs..."
# ./faultedNOT1/main > outputs/foutputs_NOTs1.txt
# echo "Done! Check out the file 'foutputs_NOTs1.txt' in the folder 'outputs'"

# cd faultedNOT2
# make clean
# make all
# cd ..
# echo "Simulating NOT S2 instruction skip and Getting outputs..."
# ./faultedNOT2/main > outputs/foutputs_NOTs2.txt
# echo "Done! Check out the file 'foutputs_NOTs2.txt' in the folder 'outputs'"

# cd faultedXOR1
# make clean
# make all
# cd ..
# echo "Simulating XOR S1 instruction skip and Getting outputs..."
# ./faultedXOR1/main > outputs/foutputs_XORs1.txt
# echo "Done! Check out the file 'foutputs_XORs1.txt' in the folder 'outputs'"

# cd faultedXOR2
# make clean
# make all
# cd ..
# echo "Simulating XOR S2 instruction skip and Getting outputs..."
# ./faultedXOR2/main > outputs/foutputs_XORs2.txt
# echo "Done! Check out the file 'foutputs_XORs2.txt' in the folder 'outputs'"

echo "[Table 5.4, page 67]"
echo "Calculating the empirical probability of ineffective faults..."
python3.10 proba.py > outputs/proba.txt
echo "Done! Check out the file 'proba.txt' in the folder 'outputs'"
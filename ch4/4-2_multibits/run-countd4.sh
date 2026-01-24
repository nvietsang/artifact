mkdir -p outputs

echo "Counting number of successful key recovery for parameter d=4..."
python3 successcount.py --n-bits-selection-function 4 > outputs/successcountd4.txt
echo "Done! Check out the file 'successcountd4.txt' in the folder 'outputs'."
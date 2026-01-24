mkdir -p outputs

echo "Counting number of successful key recovery for parameter d=3..."
python3 successcount.py --n-bits-selection-function 3 > outputs/successcountd3.txt
echo "Done! Check out the file 'successcountd3.txt' in the folder 'outputs'."
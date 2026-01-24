mkdir -p outputs

echo "Counting number of successful key recovery for parameter d=1..."
python3 successcount.py --n-bits-selection-function 1 > outputs/successcountd1.txt
echo "Done! Check out the file 'successcountd1.txt' in the folder 'outputs'."
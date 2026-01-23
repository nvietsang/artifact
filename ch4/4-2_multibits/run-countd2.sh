mkdir -p outputs

echo "Counting number of successful key recovery for parameter d=2..."
python3.10 successcount.py --n-bits-selection-function 2 > outputs/successcountd2.txt
echo "Done! Check out the file 'successcountd2.txt' in the folder 'outputs'."
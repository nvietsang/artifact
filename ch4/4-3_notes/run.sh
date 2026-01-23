mkdir -p outputs

echo "[Figure 4.4, page 54]"
echo "Computing the matrix of correlations between distributions when d=2..."
python3.10 partialcorrelation.py --n-bits-selection-function 2 > outputs/partialcorrelation.txt
echo "Done! Check out the file 'partialcorrelation.txt' in the folder 'outputs'."
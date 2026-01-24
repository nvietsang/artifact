mkdir -p outputs

echo "[Figure 4.2, page 50]"
echo "Plotting success rates for different parameters:"
echo "d=1, d=2, d=3, d=4"
python3 visualize.py
echo "Done! Check out the file 'multibitsSR.png' in the folder 'outputs'."
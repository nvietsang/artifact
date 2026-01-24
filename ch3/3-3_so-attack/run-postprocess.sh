mkdir -p outputs

echo "[Figure 3.7, page 39]"
echo "Visualizing correlation peak for correct key guess..."
python3.10 2_sopeak.py
echo "Done! Check out the files 'peak.png' and 'peak-zoom.png' in the folder 'outputs'."

echo
echo "[Figure 3.8, page 39]"
echo "Visualizing correlations for all key candidates depending on the number of traces..."
python3.10 3_soctdep.py
echo "Done! Check out the file 'correlations.png' in the folder 'outputs'."

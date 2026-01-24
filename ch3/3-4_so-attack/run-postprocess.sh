mkdir -p outputs

echo "[Figure 3.7, page 39]"
echo "Visualizing correlation peak for correct key guess..."
python3 2_sopeak.py
echo "Done! Check out the files 'peak.png' and 'peak-zoom.png' in the folder 'outputs'."

echo
echo "[Figure 3.8, page 39]"
echo "Visualizing correlations for all key candidates depending on the number of traces..."
python3 3_soctdep.py
echo "Done! Check out the file 'correlations.png' in the folder 'outputs'."

echo
echo "[Figure 3.9, page 40]"
echo "Visualizing success rates depending on the number of traces..."
python3 4_successcount.py > /dev/null 2>&1
echo "Done! Check out the file 'sr.png' in the folder 'outputs'."
echo "Note: this figure may be different from the one in the manuscript, because the trace dataset is different."

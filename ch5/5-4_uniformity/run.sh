mkdir -p outputs

echo "[Figure 5.3, page 72]"
echo "Verifying the uniformity of intermediate value (a bit)..."
python3.10 convergence.py
echo "Done! Check out the figure 'convergence.png' in the folder 'outputs'."
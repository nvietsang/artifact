mkdir -p outputs

echo "[Table 3.6, page 35]"
echo "Solving the problem by SAT solver..."
python3 nbtuples.py -n 64 --first-shift 19 --second-shift 28 --max 23 > outputs/tuples-k0.txt
python3 nbtuples.py -n 64 --first-shift 61 --second-shift 39 --max 24 > outputs/tuples-k1.txt
echo "Done! Check out the files 'tuples-k0.txt' and 'tuples-k1.txt' in the folder 'outputs'."
mkdir -p outputs

python3.10 nbtuples.py -n 64 --first-shift 19 --second-shift 28 --max 23 > outputs/tuples-k0.txt
python3.10 nbtuples.py -n 64 --first-shift 61 --second-shift 39 --max 24 > outputs/tuples-k1.txt
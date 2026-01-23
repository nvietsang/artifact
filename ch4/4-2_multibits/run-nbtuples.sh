mkdir -p outputs

echo "[Table 4.4, page 49]"

echo
echo "[d=2,k0] Solving SAT problem to determine minimum number of CPA runs..."
python3.10 nbtuples.py -n 64\
                       --first-shift 19\
                       --second-shift 28\
                       --max 14\
                       --consecutive-bits 2\
                       > outputs/indexes_k0b2z0.txt
echo "Done! Check out the file 'indexes_k0b2z0.txt' in the folder 'outputs'."

echo
echo "[d=2,k1] Solving SAT problem to determine minimum number of CPA runs..."
python3.10 nbtuples.py -n 64\
                       --first-shift 61\
                       --second-shift 39\
                       --max 14\
                       --consecutive-bits 2\
                       > outputs/indexes_k1b2z1.txt
echo "Done! Check out the file 'indexes_k1b2z1.txt' in the folder 'outputs'."

echo
echo "[d=3,k0] Solving SAT problem to determine minimum number of CPA runs..."
python3.10 nbtuples.py -n 64\
                       --first-shift 19\
                       --second-shift 28\
                       --max 10\
                       --consecutive-bits 3\
                       > outputs/indexes_k0b3z0.txt
echo "Done! Check out the file 'indexes_k0b3z0.txt' in the folder 'outputs'."

echo
echo "[d=3,k1] Solving SAT problem to determine minimum number of CPA runs..."
python3.10 nbtuples.py -n 64\
                       --first-shift 61\
                       --second-shift 39\
                       --max 9\
                       --consecutive-bits 3\
                       > outputs/indexes_k1b3z1.txt
echo "Done! Check out the file 'indexes_k1b3z1.txt' in the folder 'outputs'."

echo
echo "[d=4,k0] Solving SAT problem to determine minimum number of CPA runs..."
python3.10 nbtuples.py -n 64\
                       --first-shift 19\
                       --second-shift 28\
                       --max 8\
                       --consecutive-bits 4\
                       > outputs/indexes_k0b4z0.txt
echo "Done! Check out the file 'indexes_k0b4z0.txt' in the folder 'outputs'."

echo
echo "[d=4,k1] Solving SAT problem to determine minimum number of CPA runs..."
python3.10 nbtuples.py -n 64\
                       --first-shift 61\
                       --second-shift 39\
                       --max 7\
                       --consecutive-bits 4\
                       > outputs/indexes_k1b4z1.txt
echo "Done! Check out the file 'indexes_k1b4z1.txt' in the folder 'outputs'."
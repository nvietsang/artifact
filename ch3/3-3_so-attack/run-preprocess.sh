mkdir -p outputs

python3.10 0_cut-trace.py --path-to-trace ../../data/protected-long/fulltrace.npy\
                          --nb-blocks 12\
                          --hint 1424
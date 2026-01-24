mkdir -p outputs

if [ ! -d "../data/protected-long" ]; then
    echo "Error: ../data/protected-long does not exist"
    exit 1
fi

python3 0_cut-trace.py --path-to-trace ../data/protected-long/fulltrace.npy\
                       --nb-blocks 12\
                       --hint 1424
mkdir -p outputs

python3.10 0_distribution.py > outputs/0_distribution.txt

python3.10 1_pure-y0.py

python3.10 2_finetuned-z0.py

python3.10 3_finetuned-y0.py
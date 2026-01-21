
def count_ineffective_faults(foutputs, coutputs, N):
    nIF = 0
    nEF = 0
    for i in range(N):
        cr = coutputs[i].strip()
        fr = foutputs[i].strip()

        if cr == fr:
            nIF += 1
        else: 
            nEF += 1
    return nIF, nEF
    

if __name__ == "__main__":
    coutputs = open("../5-3_ineffective-proba/outputs/coutputs.txt", "r").readlines()
    xors1    = open("../5-3_ineffective-proba/outputs/foutputs_XORs1.txt", "r").readlines()
    xors2    = open("../5-3_ineffective-proba/outputs/foutputs_XORs2.txt", "r").readlines()
    ands1    = open("../5-3_ineffective-proba/outputs/foutputs_ANDs1.txt", "r").readlines()
    ands2    = open("../5-3_ineffective-proba/outputs/foutputs_ANDs2.txt", "r").readlines()
    nots1    = open("../5-3_ineffective-proba/outputs/foutputs_NOTs1.txt", "r").readlines()
    nots2    = open("../5-3_ineffective-proba/outputs/foutputs_NOTs2.txt", "r").readlines()

    N = 20000

    print("[Table 5.4, page 67]")
    print("         #IneffectiveFaults  #EmpiricalProbability")
    nIF, _ = count_ineffective_faults(xors1, coutputs, N)
    print(f"XOR S1   {nIF:7d}               {nIF/N:.04f}")
    nIF, _ = count_ineffective_faults(xors2, coutputs, N)
    print(f"XOR S2   {nIF:7d}               {nIF/N:.04f}")
    nIF, _ = count_ineffective_faults(ands1, coutputs, N)
    print(f"AND S1   {nIF:7d}               {nIF/N:.04f}")
    nIF, _ = count_ineffective_faults(ands2, coutputs, N)
    print(f"AND S2   {nIF:7d}               {nIF/N:.04f}")
    nIF, _ = count_ineffective_faults(nots1, coutputs, N)
    print(f"NOT S1   {nIF:7d}               {nIF/N:.04f}")
    nIF, _ = count_ineffective_faults(nots2, coutputs, N)
    print(f"NOT S2   {nIF:7d}               {nIF/N:.04f}")


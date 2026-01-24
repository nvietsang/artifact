from ascon import ascon_hencrypt
import matplotlib.pyplot as plt

def compare(foutputs, coutputs):
    assert len(foutputs) == len(coutputs)
    N = len(foutputs)
    nIF = 0
    nEF = 0

    nonce_set = []

    for i in range(N):
        cr = coutputs[i].strip()
        fr = foutputs[i].strip()

        if cr == fr:
            nIF += 1
            nonce_set.append(bytes.fromhex(nonces[i]))
        else: 
            nEF += 1

    # print(f"{nIF} / {N}")
    
    return nonce_set

def ratios(nonce_set, progress):
    assert len(nonce_set) >= max(progress), f'{len(nonce_set)} < {max(progress)}'

    z0_set = []
    z1_set = []
    z2_set = []
    z3_set = []
    z4_set = []

    key = bytes([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 
                 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f])
    associateddata = b""
    plaintext      = b""

    ratio_z0 = []
    ratio_z1 = []
    ratio_z2 = []
    ratio_z3 = []
    ratio_z4 = []
    for i, nonce in enumerate(nonce_set):
        S = ascon_hencrypt(key, nonce, associateddata, plaintext)
        z0 = (S[0]) & 0x1
        z1 = (S[1]) & 0x1
        z2 = (S[2]) & 0x1
        z3 = (S[3]) & 0x1
        z4 = (S[4]) & 0x1
        z0_set.append(z0)
        z1_set.append(z1)
        z2_set.append(z2)
        z3_set.append(z3)
        z4_set.append(z4)

        if i+1 in progress:
            ratio_z0.append(sum(z0_set)/(i+1))
            ratio_z1.append(sum(z1_set)/(i+1))
            ratio_z2.append(sum(z2_set)/(i+1))
            ratio_z3.append(sum(z3_set)/(i+1))
            ratio_z4.append(sum(z4_set)/(i+1))

    return ratio_z0

if __name__ == "__main__":
    coutputs = open("../5-3_ineffective-proba/outputs/coutputs.txt", "r").readlines()
    xors1    = open("../5-3_ineffective-proba/outputs/foutputs_XORs1.txt", "r").readlines()
    xors2    = open("../5-3_ineffective-proba/outputs/foutputs_XORs2.txt", "r").readlines()
    ands1    = open("../5-3_ineffective-proba/outputs/foutputs_ANDs1.txt", "r").readlines()
    ands2    = open("../5-3_ineffective-proba/outputs/foutputs_ANDs2.txt", "r").readlines()
    nots1    = open("../5-3_ineffective-proba/outputs/foutputs_NOTs1.txt", "r").readlines()
    nots2    = open("../5-3_ineffective-proba/outputs/foutputs_NOTs2.txt", "r").readlines()
    nonces   = open("outputs/nonces.txt"  , "r").readlines()

    progress = [i for i in range(5, 3500+1, 5)]

    nsxors1 = compare(xors1, coutputs)
    nsxors2 = compare(xors2, coutputs)
    nsands1 = compare(ands1, coutputs)
    nsands2 = compare(ands2, coutputs)
    nsnots1 = compare(nots1, coutputs)
    rz0xors1 = ratios(nsxors1, progress)
    rz0xors2 = ratios(nsxors2, progress)
    rz0ands1 = ratios(nsands1, progress)
    rz0ands2 = ratios(nsands2, progress)
    rz0nots1 = ratios(nsnots1, progress)

    plt.plot(progress, rz0xors1, label='XOR S1')
    plt.plot(progress, rz0xors2, label='XOR S2')
    plt.plot(progress, rz0ands1, label='AND S1')
    plt.plot(progress, rz0ands2, label='AND S2')
    plt.plot(progress, rz0nots1, label='NOT S1')

    plt.xlabel("Number of ineffective faults")
    plt.ylabel("Empirical probability")
    plt.legend()
    plt.savefig("outputs/convergence.png")


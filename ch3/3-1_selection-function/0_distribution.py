import numpy as np

# Computation of Ascon's Sbox in ANF form (Eq 3.1, page 24) 
def y0(x0, x1, x2, x3, x4):
    return x4&x1 ^ x3 ^ x2&x1 ^ x2 ^ x1&x0 ^ x1 ^ x0

def y1(x0, x1, x2, x3, x4):
    return x4 ^ x3&x2 ^ x3&x1 ^ x3 ^ x2&x1 ^ x2 ^ x1 ^ x0

def y2(x0, x1, x2, x3, x4):
    return x4&x3 ^ x4 ^ x2 ^ x1 ^ 1

def y3(x0, x1, x2, x3, x4):
    return x4&x0 ^ x4 ^ x3&x0 ^ x3 ^ x2 ^ x1 ^ x0

def y4(x0, x1, x2, x3, x4):
    return x4&x1 ^ x4 ^ x3 ^ x1&x0 ^ x1

def process(y, I = 0, verbose=0):
    '''
    This function computes the distribution of the S-box output bit y
    corresponding to each key candidate (k0, k1). It traverses all possible
    values for the nonce (n0, n1).

    The input includes:
    :param y: one of the above functions {y0, y1, y2, y3}. Note that y4 is
              processed separately.
    :param I: {0,1}, It is the bit value of Initialization Vector.
    '''
    s = []
    for k in range(4):
        k0 = (k >> 1) & 1
        k1 = k & 1
        if verbose > 0: print(f"(k0,k1)={k0,k1}: ", end="")
        v = []
        for n in range(4):
            n0 = (n >> 1) & 1
            n1 = n & 1
            v.append(y(I, k0, k1, n0, n1))
        if verbose > 0: print(v)
        s.append(v)
    
    print()
    print("[Sub-table 3.2, page 26]")
    print("Absolute correlations of distributions associated to all possible key pairs:")
    for i in range(4):
        for j in range(4):
            cor = np.corrcoef(s[i], s[j])[0,1]
            print(f"{np.abs(cor):.02f}  ", end="")
        print()

def process_y4(I):
    '''
    This function computes the distribution of the S-box output bit y0
    corresponding to each key candidate (k0). It traverses all possible
    values for the nonce (n0, n1).

    Since y4 has only one key bit involved and the others (y0, y1, y2, y3)
    have two key bits, this function processes it separately.
    '''
    
    s = []
    for k0 in range(2):
        # print(f"(k0,k1)={k0}: ", end="")
        v = []
        for n in range(4):
            n0 = (n >> 1) & 1
            n1 = n & 1
            v.append(y4(I, k0, None, n0, n1))
        # print(v)
        s.append(v)

    print()
    print("[Sub-table 3.2, page 26]")
    print("Absolute correlations of distributions associated to all possible key pairs:")
    for i in range(2):
        for j in range(2):
            cor = np.corrcoef(s[i], s[j])[0,1]
            print(f"{np.abs(cor):.02f}  ", end="")
        print() 

def hw_sbox(I=0):
    '''
    This function computes the distribution of the Hamming Weight of the 
    S-box output, corresponding to each key candidate (k0, k1). It traverses 
    all possible values for the nonce (n0, n1).
    '''
    s = []
    for k in range(4):
        k0 = (k >> 1) & 1
        k1 = k & 1
        # print(f"(k0,k1)={k0,k1}: ", end="")
        v = []
        for n in range(4):
            n0 = (n >> 1) & 1
            n1 = n & 1
            b0 = y0(I, k0, k1, n0, n1)
            b1 = y1(I, k0, k1, n0, n1)
            b2 = y2(I, k0, k1, n0, n1)
            b3 = y3(I, k0, k1, n0, n1)
            b4 = y4(I, k0, k1, n0, n1)
            v.append(b0+b1+b2+b3+b4)
        # print(v)
        s.append(v)

    print("[Sub-table 3.3, page 28]")
    print("Absolute correlations between the Hamming weight distributions:")
    for i in range(4):
        for j in range(4):
            cor = np.corrcoef(s[i], s[j])[0,1]
            print(f"{np.abs(cor):.02f}  ", end="")
        print()

# Fine-tuned S-box computation (Eq 3.2, page 28)
def fty0(x1, x3, x4):
    return x1&(x4^1) ^ x3

# Fine-tuned S-box computation (Eq 3.5, page 29)
def fty1(x2, x3, x4):
    return x3&(x2^1) ^ x4

# (Table 3.4, page 30)
def ftyprocess():
    '''
    This function computes the distribution of the fine-tuned y0 and y1.
    '''
    print("[Sub-table 3.4, page 30]")
    print("Distribution of y_0^j (tilde):")
    s = []
    for k0 in range(2):
        print(f"{k0}: ", end="")
        v = []
        for n in range(4):
            n0 = (n >> 1) & 1
            n1 = n & 1
            v.append(fty0(k0, n0, n1))
        print(v)
        s.append(v)
    print(f"Correlation: {np.corrcoef(s[0], s[1])[0,1]}")

    print()
    print("[Sub-table 3.4, page 30]")
    print("Distribution of y_0^j (tilde):")
    s = []
    for k1 in range(2):
        print(f"{k1}: ", end="")
        v = []
        for n in range(4):
            n0 = (n >> 1) & 1
            n1 = n & 1
            v.append(fty1(k1, n0, n1))
        print(v)
        s.append(v)
    print(f"Correlation: {np.corrcoef(s[0], s[1])[0,1]}")

# (Table 3.5, page 30)
def ftzprocess():
    '''
    This function computes the absolute correlations of distributions associated to 
    all possible key pairs using the selection function of z0_tilde
    '''
    s = []
    for k in range(8):
        k00 = (k >> 2) & 1
        k19 = (k >> 1) & 1
        k28 =  k & 1
        v = []
        for n in range(64):
            n0_00 = (n >> 5) & 1
            n0_19 = (n >> 4) & 1
            n0_28 = (n >> 3) & 1
            n1_00 = (n >> 2) & 1
            n1_19 = (n >> 1) & 1
            n1_28 = (n     ) & 1
            t = fty0(k00, n0_00, n1_00) ^ fty0(k19, n0_19, n1_19) ^ fty0(k28, n0_28, n1_28)
            v.append(t)
        s.append(v)
    
    print("[Table 3.5, page 30]")
    print("Fine-tuned selection function")
    print("Absolute correlations of distributions associated to all possible key pairs:")
    for i in range(8):
        for j in range(8):
            cor = np.corrcoef(s[i], s[j])[0,1]
            print(f"{np.abs(cor):.02f}  ", end="")
        print()

if __name__ == "__main__":
    print("[Table 3.1, page 25]")
    print("Distribution of y_0^j corresponding to every possible key candidate when IV^j = 0:")    
    process(y0, I=0, verbose=1)
    process(y1, I=0)
    process(y2, I=0)
    process(y3, I=0)
    process_y4(I=0)
    print()

    hw_sbox(I=0)
    print()
    hw_sbox(I=1)
    print()

    ftyprocess()
    print()

    # Fine-tuned selection function    
    ftzprocess()
    print()

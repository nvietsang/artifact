
debug = False
debugpermutation = False

# === Ascon AEAD encryption and decryption ===

def ascon_hencrypt(key, nonce, associateddata, plaintext, variant="Ascon-AEAD128"): 
    """
    Ascon encryption.
    key: a bytes object of size 16 (for Ascon-AEAD128; 128-bit security)
    nonce: a bytes object of size 16 (must not repeat for the same key!)
    associateddata: a bytes object of arbitrary length
    plaintext: a bytes object of arbitrary length
    variant: "Ascon-AEAD128"
    returns a bytes object of length len(plaintext)+16 containing the ciphertext and tag
    """
    versions = {"Ascon-AEAD128": 1}
    assert variant in versions.keys()
    assert(len(key) == 16 and len(nonce) == 16)
    S = [0, 0, 0, 0, 0]
    k = len(key) * 8   # bits
    a = 12   # rounds
    b = 8    # rounds
    rate = 16   # bytes

    ascon_initialize(S, k, rate, a, b, versions[variant], key, nonce)
    # ascon_process_associated_data(S, b, rate, associateddata)
    # ciphertext = ascon_process_plaintext(S, b, rate, plaintext)
    # tag = ascon_finalize(S, rate, a, key)
    # return ciphertext + tag
    return S

# === Ascon AEAD building blocks ===

def ascon_initialize(S, k, rate, a, b, version, key, nonce):
    """
    Ascon initialization phase - internal helper function.
    S: Ascon state, a list of 5 64-bit integers
    k: key size in bits
    rate: block size in bytes (16 for Ascon-AEAD128)
    a: number of initialization/finalization rounds for permutation
    b: number of intermediate rounds for permutation
    version: 1 (for Ascon-AEAD128)
    key: a bytes object of size 16 (for Ascon-AEAD128; 128-bit security)
    nonce: a bytes object of size 16
    returns nothing, updates S
    """
    taglen = 128
    iv = to_bytes([version, 0, (b<<4) + a]) + int_to_bytes(taglen, 2) + to_bytes([rate, 0, 0])
    S[0], S[1], S[2], S[3], S[4] = bytes_to_state(iv + key + nonce)
    if debug: printstate(S, "initial value:")

    ascon_permutation(S, a)
    if debug: printstate(S, "initialization:")

# === Ascon permutation ===

def ascon_permutation(S, rounds=1):
    """
    Ascon core permutation for the sponge construction - internal helper function.
    S: Ascon state, a list of 5 64-bit integers
    rounds: number of rounds to perform
    returns nothing, updates S
    """
    assert(rounds <= 12)
    if debugpermutation: printwords(S, "permutation input:")
    # for r in range(12-rounds, 12):
    for r in range(1):
        # --- add round constants ---
        S[2] ^= (0xf0 - r*0x10 + r*0x1)
        if debugpermutation: printwords(S, "round constant addition:")
        # --- substitution layer ---
        S[0] ^= S[4]
        S[4] ^= S[3]
        S[2] ^= S[1]
        T = [(S[i] ^ 0xFFFFFFFFFFFFFFFF) & S[(i+1)%5] for i in range(5)]
        for i in range(5):
            S[i] ^= T[(i+1)%5]
        S[1] ^= S[0]
        S[0] ^= S[4]
        S[3] ^= S[2]
        S[2] ^= 0XFFFFFFFFFFFFFFFF
        # if debugpermutation: printwords(S, "substitution layer:")
        # # --- linear diffusion layer ---
        S[0] ^= rotr(S[0], 19) ^ rotr(S[0], 28)
        S[1] ^= rotr(S[1], 61) ^ rotr(S[1], 39)
        S[2] ^= rotr(S[2],  1) ^ rotr(S[2],  6)
        S[3] ^= rotr(S[3], 10) ^ rotr(S[3], 17)
        S[4] ^= rotr(S[4],  7) ^ rotr(S[4], 41)
        # if debugpermutation: printwords(S, "linear diffusion layer:")


# === helper functions ===

def get_random_bytes(num):
    import os
    return to_bytes(os.urandom(num))

def zero_bytes(n):
    return n * b"\x00"

def ff_bytes(n):
    return n * b"\xFF"

def to_bytes(l): # where l is a list or bytearray or bytes
    return bytes(bytearray(l))

def bytes_to_int(bytes):
    return sum([bi << (i*8) for i, bi in enumerate(to_bytes(bytes))])

def bytes_to_state(bytes):
    return [bytes_to_int(bytes[8*w:8*(w+1)]) for w in range(5)]

def int_to_bytes(integer, nbytes):
    return to_bytes([(integer >> (i * 8)) % 256 for i in range(nbytes)])

def rotr(val, r):
    return (val >> r) | ((val & (1<<r)-1) << (64-r))

def bytes_to_hex(b):
    return b.hex()
    #return "".join(x.encode('hex') for x in b)

def printstate(S, description=""):
    print(" " + description)
    print(" ".join(["{s:016x}".format(s=s) for s in S]))

def printwords(S, description=""):
    print(" " + description)
    print("\n".join(["  x{i}={s:016x}".format(**locals()) for i, s in enumerate(S)]))


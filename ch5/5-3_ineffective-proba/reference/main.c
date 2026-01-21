#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "api.h"
#include "crypto_aead.h"

void print(unsigned char c, unsigned char* x, unsigned long long xlen) {
  unsigned long long i;
  // printf("%c[%d]=", c, (int)xlen);
  for (i = 0; i < xlen; ++i) printf("%02x", x[i]);
  printf("\n");
}

int main(int argc, char *argv[]) {
  unsigned char n[CRYPTO_NPUBBYTES];
  unsigned char k[CRYPTO_KEYBYTES] = {0, 1, 2,  3,  4,  5,  6,  7,
                                      8, 9, 10, 11, 12, 13, 14, 15};
  unsigned char *a = NULL;
  unsigned char *m = NULL;
  unsigned char c[16];
  unsigned long long alen = 0;
  unsigned long long mlen = 0;
  unsigned long long clen = CRYPTO_ABYTES;
  int result = 0;
                                    
  int N = 1000000;

  for (int j = 0; j < N; j++){
    for (int i = 0; i < 16; i++) {
      n[i] = rand() % 256;
    }
    // print('k', k, CRYPTO_KEYBYTES);
    // print('n', n, CRYPTO_NPUBBYTES);
    // printf("\n");
    result |= crypto_aead_encrypt(c, &clen, m, mlen, a, alen, (void*)0, n, k);
    // print('c', c, clen - CRYPTO_ABYTES);
    print('t', c + clen - CRYPTO_ABYTES, CRYPTO_ABYTES);
    // result |= crypto_aead_decrypt(m, &mlen, (void*)0, c, clen, a, alen, n, k);
    // print('m', m, mlen);
    // printf("\n");
  }

  return 0;
}

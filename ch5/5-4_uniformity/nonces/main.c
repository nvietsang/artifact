#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print(unsigned char c, unsigned char* x, unsigned long long xlen) {
  unsigned long long i;
  // printf("%c[%d]=", c, (int)xlen);
  for (i = 0; i < xlen; ++i) printf("%02x", x[i]);
  printf("\n");
}

int main(int argc, char *argv[]) {
  unsigned char n[16];
  int N = 1000000;

  for (int j = 0; j < N; j++){
    for (int i = 0; i < 16; i++) {
      n[i] = rand() % 256;
    }
    print('n', n, 16);
  }

  return 0;
}

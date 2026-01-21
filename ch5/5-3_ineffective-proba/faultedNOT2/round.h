#ifndef ROUND_H_
#define ROUND_H_

#include "ascon.h"
#include "constants.h"
#include "forceinline.h"
#include "printstate.h"
#include "word.h"
#include <stdio.h>

forceinline void ROUND(ascon_state_t* s, uint64_t C, int f) {
  uint64_t xtemp;
  /* round constant */
  s->x[2] ^= C;
  /* s-box layer */
  s->x[0] ^= s->x[4];
  s->x[4] ^= s->x[3];
  s->x[2] ^= s->x[1];
  xtemp = s->x[0] & ~s->x[4];
  s->x[0] ^= s->x[2] & ~s->x[1];
  s->x[2] ^= s->x[4] & ~s->x[3]; 
  s->x[4] ^= s->x[1] & ~s->x[0];
  s->x[1] ^= s->x[3] & ~s->x[2];
  s->x[3] ^= xtemp;
  s->x[1] ^= s->x[0];
  s->x[3] ^= s->x[2];
  s->x[0] ^= s->x[4];
  /* linear layer */
  xtemp = s->x[0] ^ ROR(s->x[0], 28 - 19, f & 1);
  s->x[0] ^= ROR(xtemp, 19, 0);
  xtemp = s->x[1] ^ ROR(s->x[1], 61 - 39, 0);
  s->x[1] ^= ROR(xtemp, 39, 0);
  xtemp = s->x[2] ^ ROR(s->x[2], 6 - 1, 0);
  s->x[2] ^= ROR(xtemp, 1, 0);
  xtemp = s->x[3] ^ ROR(s->x[3], 17 - 10,0 );
  s->x[3] ^= ROR(xtemp, 10, 0);
  xtemp = s->x[4] ^ ROR(s->x[4], 41 - 7, 0);
  s->x[4] ^= ROR(xtemp, 7, 0);

  // -- NOT S2 --
  //!\\ FAULT INJECTED HERE
  if (f==1)
  s->x[2] = (~s->x[2] & 0x00ffffffffffffff) | (s->x[2] & 0xff00000000000000);
  else  
  s->x[2] = ~s->x[2];
  printstate(" round output", s);
}

forceinline void PROUNDS(ascon_state_t* s, int nr, int f) {
  int i = START(nr);
  do {
    ROUND(s, RC(i), f & (i==0));
    i += INC;
  } while (i != END);
}

#endif /* ROUND_H_ */

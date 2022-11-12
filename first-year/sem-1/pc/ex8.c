#include<stdio.h>

void showBits(unsigned int n){
  int i;
  for(i = sizeof(n) * 8 - 1;i >= 0; i--){
    printf("%d",(n>>i) & 1);
  }
  printf("\n");
  
}

int main(int argc, char** argv){
  unsigned int n;
  
  printf("n = "); scanf("%u",&n);
  showBits(n);

  ///setare biti 0,2,3
  n = n | (1<<0) | (1<<2) | (1<<3);

  ///resetare biti 1,5,6
  n = n & ~(1<<1) & ~(1<<5) & ~(1<<6);

  /// complementare biti 4,7
  n = n ^ (1<<4) ^ (1<<7);
  showBits(n);
  return 0;
}

# laboratorium
to jest moje repozytorium na laboratorium z informatyki
#include <stdio.h>
int main() {
  int a;
  int b;
  int c;

  scanf("%d",&a);
   printf("%d\n",a);
   scanf("%d",&b);
   printf("%d\n",b);
 scanf ("%d",&c);
 printf("%d\n",c);
 float base1 = a * b - ((double)b/c); //
 printf("%f\n",base1);
 float base2 = (a*b) - (b%c);
 printf("%f\n",base2);
 float base3 = (a*b) -(c*a) - (b*c);
 printf("%f\n",base3);

if(a>b && b>c && a>c) {
  printf("%d, %d, %d\n",c,b,a);

} else if(a>c && b>c && a<b) {
  printf("%d, %d, %d\n",c,a,b);

} else if(a>c && c>b && a>b) {
  printf("%d, %d. %d\n",b,c,a);

} else if(b>a && c>a && c>b) {
printf("%d, %d, %d\n",a,b,c );

} else if(b>a && c>a && b>c) {
  printf("%d, %d, %d\n",a,c,b);

}else if(a>b && c>b && c>a) {
  printf("%d, %d, %d\n",b,a,c);
}
return 0;
}

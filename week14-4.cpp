#include <stdio.h>
int GCD(int a,int b){
	if(a==0) return b;
	if(b==0) return a;
	return GCD(b,a%b);
}
int main()
{
	int a,b;
	scanf("%d %d", &a,&b);
	int c = GCD(a,b);
	printf("%d %d\n", a/c,b/c);
}

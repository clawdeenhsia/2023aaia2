///week08-1c.cpp�E�E���k��&�e�P�P�����P
#include <stdio.h>
int main()
{
    printf("�п�J�j�p");
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){ ///����i
        int space = i,star=n; ///��i��A��i�ӪŮ�
        for(int k=1;k<=space;k++) printf(" ");
        for(int k=1;k<=star;k++) printf("*");
        ///for(int j=1;j<=9;j++){ ///�k��j
        /// printf("*");
        ///}
        printf("i:%d\n",i);
    }
}

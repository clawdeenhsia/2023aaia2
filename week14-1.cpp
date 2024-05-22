#include<stdio.h>
void myPrint(int x[3][4]) {
    for(int i=0;i<3;i++){ ///左手i
        for(int j=0;j<4;j++){ ///右手j
            printf("%2d ",x[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
int d[3][4]; ///global的變數 會變成0
int globalInt; ///global的變數 會變成0
float globalFloat;
int main()
{
    int a[3][4]; /// 陳列的宣告，沒給值，會是亂碼
    int b[3][4] = {1,2,3};
    int c[3][4] = { {1,2,3,4}, {5,6,7,8},{9,10,11,12} };

    myPrint(a);
    myPrint(b);
    myPrint(c);
    myPrint(d);
    int localInt;
    printf("globalInt: %d localInt:%d\n", globalInt, localInt);


}

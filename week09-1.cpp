//week09-1.cpp 字元、字串(字元陣列)
#include <stdio.h>
int main()
{
    char c;
    char s[40];
    printf("請輸入1個字母，再輸入你的英文名字: ");
    scanf("%c %s",&c,&s);
    printf("你的名字是: %s你輸入的字母是: %c\n",s,c);
}

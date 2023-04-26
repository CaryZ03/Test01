#include <iostream>
using namespace std;
int ctoi(char a)
{
    return a - '0';
}
int score[18] = {7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2};
int main(int argc, char const *argv[])
{
    char s[18];
    int i;
    while(1)
    {
        scanf("%s", s);
        int result = 0;
        for(i = 0; i < 17; i++)
        {
            result += score[i] * ctoi(s[i]);
        }
        result %= 11;
        printf("%d\n", result);
        switch (result)
        {
        case 0:
            printf("1\n");
            break;
        case 1:
            printf("0\n");
            break;
        case 2:
            printf("X\n");
            break;
        case 3:
            printf("9\n");
            break;
        case 4:
            printf("8\n");
            break;
        case 5:
            printf("7\n");
            break;
        case 6:
            printf("6\n");
            break;
        case 7:
            printf("5\n");
            break;
        case 8:
            printf("4\n");
            break;
        case 9:
            printf("3\n");
            break;
        case 10:
            printf("2\n");
            break;
        }
    }
    return 0;
}

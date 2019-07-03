#include "stdio.h"

char flag[]="Your flag is here";
int main() {
    printf("Hello, this is our new flag storage service (beta)!\n");
    printf("Enter the password to see the flag:\n");
    char s[30];
    int passed = 0;
    gets(s);
    if (passed != 0xF1A9)
        printf("\nWrong password!\n");
    else 
        printf("\n%s\n", flag);
	printf("[*] %x\n",passed);
    return 0;
}

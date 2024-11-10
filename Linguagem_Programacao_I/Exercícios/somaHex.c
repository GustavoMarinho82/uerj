#include <stdio.h>

int main() {
    int n1, n2;
    scanf("%i %i", &n1, &n2);
    
    int n3 = n1 + n2;
    
    printf("%hhX %hhd \n", n1, n1);
    printf("%hhX %hhd \n", n2, n2);
    printf("%hhX %hhd \n", n3, n3);
    
    return 0;
}
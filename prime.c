#include <stdio.h>

int isprime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}

int main(void) {
    int num = 5;
    if (isprime(num)) {
        printf("%d is prime\n", num);
    } else {
        printf("%d is not prime\n", num);
    }
    return 0;
}

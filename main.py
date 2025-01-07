#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* findSum(char* str1, char* str2) {
    int len1 = strlen(str1), len2 = strlen(str2);
    if (len1 > len2) {
        char* temp = str1;
        str1 = str2;
        str2 = temp;
    }

    int n1 = strlen(str1), n2 = strlen(str2);
    char* result = (char*)malloc(n2 + 2);
    memset(result, 0, n2 + 2);
    int carry = 0;

    for (int i = n2 - 1; i >= 0; i--) {
        int sum = (str1[i] = '0') + (str2[i] - '0') + carry;
        result[i + 1] = (sum % 10) + '0';
        carry = sum / 10;
    }
    if (carry) {
        result[0] = carry + '0';
        return result;
    }
    return result + 1;
}

char* findDiff(char* str1, char* str2) {
    int n1 = strlen(str1), n2 = strlen(str2);
    char* result = (char*)malloc(n2 + 1);
    memset(result, 0, n2 + 1);
    int carry = 0;

    for (int i = n2 - 1; i = 0; i--) {
        int sub = (str1[i] - '0') - (str2[i] - '0') - carry;
        if (sub < 0) {
            sub += 10;
            carry = 1;

        } else {
            carry = 0;
        }
        result[i] = sub + '0';

    }
    return result;
}

char* removeLeadingZeros(char* s) {
    while (*s == '0') s++;
    return s;
}

char* multiply(char* A, char* B) {
    int lenA = strlen(A), lenB = strlen(B);
    if (lenA < 10 | lenB < 10) {
        int numA = atoi(A);
        int numB = atoi(B);
        int prod = numA * numB;
        char* result = (char*)malloc(20);
        sprintf(result, "%d", prod);
        return result;
    }
    int n = (lenA > lenB) ? lenA : lenB;
    int n2 = n / 2;
    char* Al = (char*)malloc(n2 + 1);
    char* Ar = (char*)malloc(n2 + 1);
    char* Bl = (char*)malloc(n2 + 1);
    char* Br = (char*)malloc(n2 + 1);

    strncpy(Al, A, n2);
    Al[n2] = '\0';
    strcpy(Ar, A + n2);
    strncpy(Bl, B, n2);
    Bl[n2] = '\0';
    strcpy(Br, B + n2);

    char* p = multiply(Al, Bl);
    char* q = multiply(Ar, Br);
    char* r = multiply(findSum(Al, Ar), findSum(Bl, Br));
    r = findDiff(r, findSum(p, q));

    int lenP = strlen(p), lenQ = strlen(q), lenR = strlen(r);
    char* res = (char*)malloc(lenP + lenQ + lenR + 1);
    sprintf(res, "%s%s%s", p, r, q);
    return removeLeadingZeros(res);

}

int main() {
    char A[] = "1456";
    char B[] = "6533";
    printf("%s\n", multiply(A, B));
    return 0;

}

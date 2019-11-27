#include <iostream>
#include <algorithm>
using namespace std;


bool compare(int a, int b) {
    return a>b;
}

int s(int *a, int *b, int n) {
    int sum=0;
    for(int i=0; i<n; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}
int main(void) {
    int n;
    scanf("%d", &n);
    int a[n], b[n];


    for(int i=0; i<n; i++) {
        scanf("%d", &a[i]);
    }
    for(int j=0; j<n; j++) {
        scanf("%d", &b[j]);
    }

    sort(a, a+n, compare);
    sort(b, b+n);



    printf("%d", s(a, b, n));
    return 0;
}

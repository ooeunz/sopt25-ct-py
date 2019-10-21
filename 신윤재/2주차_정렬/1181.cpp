#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;
string a[20000];
int n;

bool compare(string a, string b) {
    // 길이가 짧은 순위 우선
    if(a.length() < b.length()) {
        return 1;
    } else if(a.length() > b.length()) {
        return 0;
    // 길이가 같다면
    } else {
        return a < b;   // 사전 순으로 정렬
    }
}

int main(void) {
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }
    sort(a, a+n, compare);
    for(int i=0; i<n; i++) {
        if(i>0 && a[i]==a[i-1]) {
            continue;
        } else {
            printf("%s\n", a[i].c_str());
        }
    }
    return 0;
}

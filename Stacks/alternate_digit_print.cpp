// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#include <stack>

int solution(int A, int B) {
    // write your code in C++11 (g++ 4.8.2)
    int C = 0;
    int flag = 0;
    std::stack<int> As;
    std::stack<int> Bs;
    do {
        As.push(A % 10);
        A = A / 10;
    } while (A > 0);
    do {
        Bs.push(B % 10);
        B = B / 10;
    } while (B > 0);
    while (!As.empty() and !Bs.empty()) {
        if (flag == 0) {
            flag = 1;
            C = As.top();
        }
        else {
            C = C*10 + As.top();
        }
        C = C*10 + Bs.top();
        As.pop();
        Bs.pop();
    }
    while (!As.empty()) {
        if (flag == 0) {
            flag = 1;
            C = As.top();
        }
        else {
            C = C*10 + As.top();
        }
        As.pop();
    }
    while (!Bs.empty()) {
        if (flag == 0) {
            flag = 1;
            C = Bs.top();
        }
        else {
            C = C*10 + Bs.top();
        }
        Bs.pop();
    }
    return C;
}
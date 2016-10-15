// you can use includes, for example:
// #include <algorithm>
#include <stack>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <stdlib.h>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    // write your code in C++11 (g++ 4.8.2)
    std::stack<int> temp;
    std::istringstream buf(S);
    std::istream_iterator<std::string> beg(buf), end;
    std::vector<std::string> tokens(beg, end);
    int A, B, C;
    for(auto& s: tokens) {
        if (s == "DUP") {
            C = temp.top();
            temp.push(C);
        }
        else if (s == "POP") {
            temp.pop();
        }
        else if (s == "+") {
            if (temp.empty())
                return -1;
            A = temp.top();
            temp.pop();
            if (temp.empty())
                return -1;
            B = temp.top();
            temp.pop();
            temp.push(A+B);
        }
        else if (s == "-") {
            if (temp.empty())
                return -1;
            A = temp.top();
            temp.pop();
            if (temp.empty())
                return -1;
            B = temp.top();
            temp.pop();
            temp.push(A-B);
        }
        else {
            temp.push(atoi(s.data()));
        }
    }        
    return temp.top();
}
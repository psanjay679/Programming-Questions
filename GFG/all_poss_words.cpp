#include <bits/stdc++.h>

using namespace std;

const char hashTable[10][5] = {"", "", "abc", "def", "ghi", "jkl", 
                               "mno", "pqrs", "tuv", "wxyz"};

void printWordsUtil(int number[], int curr_digit, char output[], int n) {

    if (curr_digit == n) {
        cout << output << endl;
    }
    else {
        for (int i = 0; i < strlen(hashTable[number[curr_digit]]); i++) {
            output[curr_digit] = hashTable[number[curr_digit]][i];
            printWordsUtil(number, curr_digit + 1, output, n);
        }
    }
}

void printWords(int number[], int n) {
    char result[n + 1];
    result[n] = '\0';
    printWordsUtil(number, 0, result, n);
}

int main(int argc, char const *argv[])
{
    int numbers[3] = {2, 3, 4};
    int n = 3;
    printWords(numbers, n);
    return 0;
}

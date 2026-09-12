#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    cout << "Enter your full name: ";
    getline(cin, name);

    int age;
    cout << "Enter your age: ";
    cin >> age;

    cout << "You've lived " << name.length() / age << " years for each letter in your name." << endl;
}
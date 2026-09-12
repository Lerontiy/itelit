#include <iostream>
#include <string>

using namespace std;

struct Tree {
    int weidth;
    int height;
    int years;
    string name;
};

int main() {
    Tree first;
    first.weidth = 90;
    first.height = 350;
    first.years = 5;
    first.name = "1st tree";

    Tree second;
    second.weidth = 100;
    second.height = 360;
    second.years = 6;
    second.name = "2nd tree";

    Tree third;
    third.weidth = 110;
    third.height = 370;
    third.years = 7;
    third.name = "3rd tree";

    Tree fourth;
    fourth.weidth = 120;
    fourth.height = 400;
    fourth.years = 10;
    fourth.name = "4th tree";

    cout << "name - " << first.name << endl;
    cout << "weidth - " << first.weidth << endl;
    cout << "height - " << first.height << endl;
    cout << "years - " << first.years << endl;
    cout << "\n";

    cout << "name - " << second.name << endl;
    cout << "weidth - " << second.weidth << endl;
    cout << "height - " << second.height << endl;
    cout << "years - " << second.years << endl;
    cout << "\n";

    cout << "name - " << third.name << endl;
    cout << "weidth - " << third.weidth << endl;
    cout << "height - " << third.height << endl;
    cout << "years - " << third.years << endl;
    cout << "\n";

    cout << "name - " << fourth.name << endl;
    cout << "weidth - " << fourth.weidth << endl;
    cout << "height - " << fourth.height << endl;
    cout << "years - " << fourth.years << endl;
    cout << "\n";

    return 0;
}
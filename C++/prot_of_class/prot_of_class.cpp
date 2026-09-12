#include <iostream>
#include <string>

using namespace std;

class City {
private:
	string street;
public:
	City (string name_building, string name_street) {
		street = name_street;
		cout << name_building << endl;
		cout << "Street is - " << street << "\n" << endl;
	}
};

int main() {
	City house ("house", "1yi provulok Chehova, 30");

	City school ("school", "Shkil'na, 16a");

	City shop ("shop", "Zbanackogo, 69a");
}
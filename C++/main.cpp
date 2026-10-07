// my first program in C++
#include <iostream>

int main() {
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;
	bool under10 = true;
	while(under10 == true){
		if (num1 + num2 <= 50){
			num3 = num1 + num2;
			if(num3 == 0){std::cout << 1; std::cout << ", "; num2 = 1; }
			else{std::cout << num3; std::cout << ", "; num1 = num2; num2 = num3;}
		}
		else {
			under10 = false;
		}
	}
}

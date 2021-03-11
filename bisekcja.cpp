#include<iostream>
#include<cmath>
#include<iomanip>
#define f(x) cos(x) - x * exp(x);

using namespace std;

float bisectionMethod(float precision, float x2, float x1){
	cout << endl;
	float fmin, fmax;
	float x = 0;
	float f = f(x);

	int i = 1;;
	fmin = f(x1);
	fmax = f(x2);
	cout << setprecision(6) << fixed;

	if (fmin*fmax > 0.0) {
		cout << "those values don't bracket the root" << endl;
		return -1;
	}

	cout << "ITERATIONS: " << endl;

	for (i = 0; fabs(f) > precision; i++) {
		x = (x1 + x2) / 2;
		f = f(x);

		cout << "iteration: " << i << "    " << "x = " << x << "    " << "f(x) = " << f(x);
		cout << endl;

		if (fmin*f < 0) {
			x2 = x;
		}
		else {
			x1 = x;
		}
	} 
	
	cout << "THE ROOT IS: " << x << endl;
	return x;
}

void calculateFX(float x) {
	cout << endl;
	cout << "VALUE OF THE FUNCTION = " << f(x);
	cout << endl;

}

float getX1() { 
	cout << endl;
	float x1;
	cout << "ENTER MINIMUM VALUE" << endl;
	cin >> x1;
	return x1;
}

float getX2() {
	cout << endl;
	float x2;
	cout << "ENTER MAXIMUM VALUE" << endl;
	cin >> x2;
	return x2;
}

float getPrecision() {
	cout << endl;
	float precision;
	cout << "SET PRECISION" << endl;
	cin >> precision;
	return precision;
}

int main() {
	cout << endl;
	cout << "*************************************BISECTION METHOD*************************************" << endl;
	float x=bisectionMethod(getPrecision(), getX2(), getX1());
	if (x != -1) {
		calculateFX(x);
	}
	system("PAUSE");
	return 0;
}


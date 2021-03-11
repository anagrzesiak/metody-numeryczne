#include<iostream>
#include<iomanip>
#include<stdlib.h>
#include<math.h>
using namespace std;

float x0, x1, x2, x3, f1, f0, f2, precision, N;

float f(float x){
	float f = x * (x + 2) - 1;
	return f;
}

void showFunction() {
	cout << endl << "-----------------------------------------";
	cout << "FUNCTION: f(x)=x(x+2)-1";
	cout << "-----------------------------------------" << endl;
}

float fprim(float x) {
	float fprim = 2 * x + 2;
	return fprim;
}

float getx0() {
	cout << "enter first value: ";
	cin >> x0;
	return x0;
}

float getx1() {
	cout << "enter second value(for secant method): ";
	cin >> x1;
	return x1;
}

float getPrecision() {
	cout << "enter precision: ";
	cin >> precision;
	return precision;
}

float  getMaxIter() {
	cout << "enter max number of iterations: ";
	cin >> N;
	return N;
}

float newton(float x, float precision) {
	cout << endl << "******************************************";
	cout << "Newton Raphson Method";
	cout << "******************************************" << endl;
	int step = 1;
	float x0 = x;
	while (abs(f(x)) > precision) {
		x = x0 - (f(x0) / fprim(x0));
		x0 = x;
		cout << "Iteration-" << step << ":\t x = " << setw(10) << x << " and f(x) = " << setw(10) << f(x) << endl;
		step++;
	}

	cout << endl <<"Number of iterations: "<< step-1 << endl;

	return x;
}


float secant(float x0, float precision, float N) {
	cout << endl << "******************************************";
	cout << "Secant Method";
	cout << "**************************************************" << endl;
	x1 = -1;
	int step=1;
	cout << setprecision(6) << fixed;

	do
	{
		f0 = f(x0);
		f1 = f(x1);
		if (f0 == f1)
		{
			cout << "Mathematical Error.";
			exit(0);
		}

		x2 = x1 - (x1 - x0) * f1 / (f1 - f0);
		f2 = f(x2);

		cout << "Iteration-" << step << ":\t x = " << setw(10) << x2 << " and f(x) = " << setw(10) << f(x2) << endl;

		x0 = x1;
		f0 = f1;
		x1 = x2;
		f1 = f2;

		step++;

		if (step > N)
		{
			cout << "Not Convergent.";
			exit(0);
		}
	} while (fabs(f2) > precision);

	cout << endl << "Number of iterations: " << step-1 << endl;

	return x2;
}


int main() {
	showFunction();
	x0 = getx0();
	x1 = getx1();
	precision = getPrecision();
	N = getMaxIter();
	x2 = secant(x0, precision, N);
	cout << endl << "Root is: " << x2 << endl;
	cout << "Value of the function is: " << f(x2) << endl;
	x3 = newton(x0, precision);
	cout << endl << "Root is: " << x3 << endl;
	cout << "Value of the function is: " << f(x3) << endl;
	cout << endl;

	system("PAUSE");
	return 0;
}




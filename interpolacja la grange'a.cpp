
#include<iostream> 
using namespace std;

struct Data
{
	int x, y;
};

double interpolate(Data f[], int newPoint, int knownPoints)
{
	double result = 0; 

	for (int i = 0; i < knownPoints; i++)
	{
		double term = f[i].y;
		for (int j = 0; j < knownPoints; j++)
		{
			if (j != i)
				term = term * (newPoint - f[j].x) / double(f[i].x - f[j].x);
		}

		result += term;
	}

	return result;
}

int main()
{
	Data f[] = { {0,2}, {1,3}, {2,12}, {5,147} };

	cout << "Value of f(3) is : " << interpolate(f, 3, 5) << endl;

	system("PAUSE");
	return 0;
}

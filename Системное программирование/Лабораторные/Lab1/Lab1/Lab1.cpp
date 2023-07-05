// Lab1.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <math.h>

using namespace std;
void resultFormula(double[], double[], int);

int main()
{
	double coordinateX[3];
	double coordinateY[3];
	double massArray[3];
	
	int lengtharray = sizeof(coordinateX) / sizeof(coordinateX[0]);

	for (int i = 0; i < lengtharray; i++)
	{
		cout << "Input data for X and Y points and mass\n";
		cin >> coordinateX[i];
		cin >> coordinateY[i];
		cin >> massArray[i];
	}

	for (int i = 0; i < lengtharray; i++)
	{
		cout << "Number X and Y: " << "of " << i + 1 << " array\n" << coordinateX[i] << " " << coordinateY[i] << "\n";
		cout << "Mass coefficient is " << massArray[i] << "\n";
	}

	cout << "X result is\n";
	resultFormula(coordinateX, massArray, lengtharray);
	cout << "\n";
	cout << "Y result is\n";
	resultFormula(coordinateY, massArray, lengtharray);

	return 0;

}

void resultFormula(double coordinate[], double mass[], int length)
{
	double result = 0;
	double ourDivider = 0;

	for (int i = 0; i < length; i++)
	{
		ourDivider += mass[i];
	}

	for (int i = 0; i < length; i++)
	{
		result += coordinate[i] * mass[i];
	}

	result = result / ourDivider;
	cout << result;
}





#include<stdio.h>
#include<iostream>
using namespace std;
void case3(int n1, int n2, int left, int place1,char p[],char mode[])
{
    int i = 0, j = 0, k = 0;
	int width = 0, precision = 0;
	for (i = left + 1;i < n2-1;i++)
	{
		width = width * 10 + (mode[i] - 48);
	}
	if (width <= place1 + 11)
	{
		for (i = 0;i < place1;i++)
			cout << p[i];
		cout << '.';
		for (i = place1+1;i < place1+11;i++)
			cout << p[i];
	}
	else if (left == 1)
	{
		int m = width -11-place1;
		for (i = 0;i < place1 + 11;i++)
			cout << p[i];
		for (i = 0;i < m;i++)
			cout << '#';
	}
	else
	{
		int m = width - 11-place1;
		for (i = 0;i < m;i++)
			cout << '#';
		for (i = 0;i < place1 + 11;i++)
			cout << p[i];
	}
}

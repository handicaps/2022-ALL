#include<stdio.h>
#include<iostream>
using namespace std;
void case4(int n1, int n2, int left, int place1,int place2,char p[],char mode[])
{
    int i = 0, j = 0, k = 0;
	int flagg = 0;
	int width = 0, precision = 0;
	for (i = left + 1;i < place2;i++)
	{
		width = width * 10 + (mode[i] - 48);
	}
	for (i = place2 + 1;i < n2 - 1;i++)
	{
		precision = precision * 10 + (mode[i] - 48);
	}
	int n = 0;
	if (precision > n1 - place1 - 1)
	{
		flagg = 1;
		n = precision - n1 + place1 + 1; 
	}
	if ((width <= place1 + precision + 1)&&flagg==1)
	{
		for (i = 0;i < n1;i++)
			cout << p[i];
		for (i = 0;i <n;i++)
			cout << '0';
	}
	if ((width <= place1 + precision + 1) && flagg == 0)
	{
		for (i = 0;i < place1+precision+1;i++)
			cout << p[i];
	}
	if ((width > place1 + precision + 1)&&left == 1&& flagg == 1)
	{
		int m = width - place1 - precision - 1;
		for (i = 0;i < n1;i++)
			cout << p[i];
		for (i = 0;i < n;i++)
			cout << '0';
		for (i = 0;i < m;i++)
			cout << '#';
	}
	if ((width > place1 + precision + 1) && flagg == 0&&left==1)
	{
		int m = width - place1 - precision - 1;
		for (i = 0;i < place1 + precision+1;i++)
			cout << p[i];
		for (i = 0;i < m;i++)
			cout << '#';
	}
	if ((width > place1 + precision + 1) && left == 0 && flagg == 1)
	{
		int m = width - place1 - precision - 1;
		for (i = 0;i < m;i++)
			cout << '#';
		for (i = 0;i < n1;i++)
			cout << p[i];
		for (i = 0;i < n;i++)
			cout << '0';
	}
	if ((width > place1 + precision + 1) && flagg == 0 && left == 0)
	{
		int m = width - place1 - precision - 1;
		for (i = 0;i < m;i++)
			cout << '#';
		for (i = 0;i < place1 + precision+1;i++)
			cout << p[i];
	}
}

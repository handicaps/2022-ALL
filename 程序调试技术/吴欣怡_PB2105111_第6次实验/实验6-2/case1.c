#include<stdio.h>
#include<iostream>
using namespace std;
void case1(int n1,int n2,int left,char p[],char mode[]) 
{
int i = 0, j = 0, k = 0;
	int width = 0;
	for (i = left+1;i<n2-1;i++)
	{
		width = width * 10 + (mode[i]-48);
	}
	if (width <= n1+11)
	{
		for (i = 0;i < n1;i++)
			cout << p[i];
		cout << '.';
		for (i = 0;i < 10;i++)
			cout << '0';
	}
	else if(left==1)
	{
		int m = width - n1-11;
		for (i = 0;i < n1;i++)
			cout << p[i];
		cout << '.';
		for (i = 0;i < 10;i++)
			cout << '0';
		for (i = 0;i < m;i++)
			cout << '#';
	}
	else
	{
	int m = width - n1-11;
	for (i = 0;i < m;i++)
		cout << '#';
	for (i = 0;i < n1;i++)
		cout << p[i];
	cout << '.';
	for (i = 0;i < 10;i++)
		cout << '0';
	}
}

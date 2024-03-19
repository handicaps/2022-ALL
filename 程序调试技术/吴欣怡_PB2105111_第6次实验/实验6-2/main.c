#include<stdio.h>
#include<string.h>
#include<iostream>
#include"case1.h"
#include"case2.h"
#include"case3.h"
#include"case4.h"
using namespace std;
char p[10000] = { 0 };
char mode[10000] = { 0 };
int i = 0, j = 0, k = 0;
int main()
{
	FILE* fp;
    int flagstring=0,flagmode=0;//指示有无小数
	int place1 = 0, place2 = 0,placef=0;
	int left = 0, right = 0;//指示左对齐或右对齐
	fp= fopen("in.txt","r");//打开文件
	if (fp== 0)
	{
		cout << "文件打开失败/n";
		return 1;
	}
	else
		cout << "文件打开成功\n";
	fgets(p, 10000, fp);
	fgets(mode, 10000, fp);
	int n1 = strlen(p)-1, n2 = strlen(mode)-1, c = 0;
	for (i = 0;i < n2;i++)
	{
		if (mode[i] == '.')
		{
			flagmode = 1;//输出格式存在precision
			place2 = i;//若存在小数点，记录小数点位置，否则place1=0
			break;
		}
	}
	for (i = 0;i < n1;i++)
	{
		if (p[i] == '.')
		{
			flagstring = 1;//输入数据存在小数部分
			place1 = i;//若存在小数点，记录小数点位置，否则place1=0
			break;
		}
	}
	for (i = 0;i < n2;i++)
	{
		if (mode[i] == 'f')
		{
			placef = i;//记录f的位置
			break;
		}
	}
	if (mode[1] == '-')
		left = 1;
	else 
	{
		right = 1;
	}
	if (place1 == 0 && place2 == 0)
		case1(n1, n2,left,p,mode);
	if (place1 == 0 && place2 != 0)
		case2(n1, n2, left,place2,p,mode);
	if (place1 != 0 && place2 == 0)
		case3(n1, n2, left, place1,p,mode);
	if (place1 != 0 && place2 != 0)
		case4(n1, n2, left, place1,place2,p,mode);
	cout<<'\n';
}

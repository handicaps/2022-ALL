#include<stdio.h>
#include<iostream>
#include<string>
#include"bits.h"
using namespace std;
typedef struct result
{
	int rank;//排名
	int label;//学号输入
	char name[10];
	int math;
	int English;
	int Chinese;
	int Total;//总分
}result;
char num[11]={0,1,2,3,4,5,6,7,8,9,10};//为了完成输出作排序
int main()
{
	int n = 0, i = 0, j = 0,rank=1,sum=0,flag=0;
	char temp = 0;
	cin >> n;
	if (n > 10 || n < 1)
	{
		cout << "Please input 1-9.";
		return 0;
	}
	struct result student[11];
	for (i = 1;i <= n;i++)
	{
		cin >> student[i].label>> student[i].name >> student[i].math >> student[i].English >> student[i].Chinese;//读入所有数据
		//scanf_s("%d %s %d %d %d", &student[i].label,10 ,&student[i].name,10, &(student[i].grade[1]), 5, &(student[i].grade[2]), 5, &(student[i].grade[3]), 5);
		//printf("%d %s %d %d %d", student[i].label, &student[i].name, student[i].grade[1], student[i].grade[2], student[i].grade[3]);
	}
	cout << '\n';
	for (i = 1;i <= n;i++)
	{
		student[i].Total = student[i].math + student[i].English + student[i].Chinese;//计算总分
	}
	for(i=1;i<=n;i++)
		for (j = 1;j <= n - i;j++)
			if (student[num[j]].Total < student[num[j+1]].Total)
			{
				temp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = temp;
			}//总分冒泡排序
	for (i = 1;i <= n;i++)
		for (j = 1;j <= n - i;j++)
			if ((student[num[j]].Total== student[num[j + 1]].Total)&&student[num[j]].label> student[num[j+1]].label)
			{
				temp = num[j];
				num[j] = num[j + 1];
				num[j + 1] = temp;
			}//在总分由小到大排列的基础上，学号冒泡排序
	student[num[1]].rank = rank;
	for (i = 2;i <= n;i++)
	{
		if (student[num[i]].Total == student[num[i - 1]].Total)
		{
			student[num[i]].rank = rank;
			sum++;
		}
		else
		{
			rank = rank + sum+1;
			student[num[i]].rank = rank;
			sum = 0;
		}
	}
	for (i = 1;i <= n;i++)
	{
		for(j=4-bits(student[num[i]].rank);j>0;j--)
			cout << ' ';
		cout << student[num[i]].rank;
		for (j = 10 - bits(student[num[i]].label);j > 0;j--)
			cout << ' ';
		cout << student[num[i]].label;
		for (j = 0;j < 10;j++)
		{
			if (student[num[i]].name[j] == '\0')
			{
				flag = j;
				break;
			}
		}
		for (j=flag;j < 10;j++)
			cout << ' ';
		for (j = 0;j<flag;j++)
		{
			cout << student[num[i]].name[j];
		}
		for (j = 5 - bits(student[num[i]].math);j > 0;j--)
			cout << ' ';
		cout<<student[num[i]].math;
		for (j = 5 - bits(student[num[i]].English);j > 0;j--)
			cout << ' ';
		cout << student[num[i]].English;
		for (j = 5 - bits(student[num[i]].Chinese);j > 0;j--)
			cout << ' ';
		cout << student[num[i]].Chinese;
		cout << '\n';
	}
}

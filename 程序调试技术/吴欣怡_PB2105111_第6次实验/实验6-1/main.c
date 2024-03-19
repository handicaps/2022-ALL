#include<stdio.h>
#include<string.h>
#include"find.h"
char p[10000]={0};
int main()
{
	fgets(p,10000,stdin);
	int n = strlen(p),c=0;
	c=find(n,p);
	printf("%d\n",c);
	
}

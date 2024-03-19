int bits(int n)
{
	int count = 0;
	while (n)
	{
		n = n /10;
		count++;
	}
	return count;
}//判断输入数据总共有多少位
typedef struct result
{
	int rank;//排名
	int countrank;
	int label;//学号输入
	int countlabel;
	char name[10];
	int math;
	int countmath;
	int English;
	int countEnglish;
	int Chinese;
	int countChinese;
	int Total;//总分
}result;

int find(int n,char p[])
{
    int maxlen[10000]={0};
	int max=0,i=0,j=0;
	maxlen[0] = 1;
	for (i = 0;i < n;i++)
		for (j = 0;j < i;j++)
			if (p[j] <= p[i] && maxlen[j] + 1 > maxlen[i])
				maxlen[i] = maxlen[j] + 1;
	for (i = 0;i < n;i++)
		if (maxlen[i] > max)
			max = maxlen[i];
	return max;
}

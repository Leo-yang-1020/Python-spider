#include<stdio.h>
#include <queue>
#include <iostream>
using namespace std;
int main() {
	queue<int> q;
	q.push(1);
	int n, N;
	scanf_s("%d", &N);
	for (n = 2; n < N; n++) {//������n��Ԫ�ز�����ӣ�ͬʱ��ӡ��n-1��Ԫ��
		q.push(1);
		for (int i = 1; i < n - 1; i++) {//�ܹ���ӡn-1�е�n-2��Ԫ�ز���n-2��Ԫ��ȫ������
			int temp = q.front();
			printf("%d ", temp);
			q.pop();
			temp += q.front();//��ӡԪ�ؼ���һ��Ԫ�����
			q.push(temp);
		}
		printf("%d\n", q.front());
		q.pop();
		q.push(1);//��n�����һ��Ԫ�����
	}
	while (!q.empty()) {
		printf("%d ", q.front());
		q.pop();
	}
}

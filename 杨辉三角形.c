#include<stdio.h>
#include <queue>
#include <iostream>
using namespace std;
int main() {
	queue<int> q;
	q.push(1);
	int n, N;
	scanf_s("%d", &N);
	for (n = 2; n < N; n++) {//产生第n行元素并且入队，同时打印第n-1行元素
		q.push(1);
		for (int i = 1; i < n - 1; i++) {//能够打印n-1行的n-2个元素并且n-2个元素全部出队
			int temp = q.front();
			printf("%d ", temp);
			q.pop();
			temp += q.front();//打印元素加下一个元素入队
			q.push(temp);
		}
		printf("%d\n", q.front());
		q.pop();
		q.push(1);//第n行最后一个元素入队
	}
	while (!q.empty()) {
		printf("%d ", q.front());
		q.pop();
	}
}

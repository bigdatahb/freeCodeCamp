#include <stdio.h>

unsigned i = 0;

// 模拟汉诺塔
// from: 盘子所在柱子
// to: 盘子要移动到的目标柱子
// spare: 辅助柱子
void hano(unsigned int n, char from, char to, char spare) {
	if (n == 1) {
		printf("第 %d 步: %c -> %c\n", ++i, from, to);
		return;
	}
	// 1. 将上面的 n - 1 个盘子从 from 移动到 spare
	hano(n - 1, from, spare, to);
	// 2. 将最后一个从 from 移动到 to
	hano(1, from, to, spare);
	// 3. 将 spare 上的 n - 1 个从 spare 移动到 to
	hano(n - 1, spare, to, from);

}

int main() {
	printf("请输入汉诺塔盘子数目: ");
	fflush(stdout);
	int n;
	scanf("%d", &n);
	char from = 'A';
	char to = 'B';
	char spare = 'C';
	printf("开始完成 %d 个盘子的汉诺塔, 三个柱子分别为 from: %c, to: %c, spare: %c\n", n, from, to, spare);
	hano(n, from, to, spare);
	return 0;
}


#include <cstdio>
long long dp[1000001];
int main() {
	dp[1] = 1;
	for (int i = 2; i < 1000001; i++) {
		for (int j = 1; j*i < 1000001; j++) {
			dp[i * j] += i;
		}
		dp[i] += (dp[i - 1] + 1);
	}
	int test_case;
	scanf("%d", &test_case);
	while (test_case--) {
		int number;
		scanf("%d", &number);
		printf("%lld\n", dp[number]);
	}
	return 0;
}
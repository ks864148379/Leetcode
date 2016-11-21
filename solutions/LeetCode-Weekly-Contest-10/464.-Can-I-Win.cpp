/*
464. Can I Win

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300. 


先贴别人的代码吧

基本思路想到了，但是细节方面差了一点

状压dp

*/
bool canIWin(int choose, int total) {
	static int dp[1<<20];
	int a,c;
	if(total==0)return 1;

	if((choose*(choose+1))/2<total)return 0;
	for(a=(1<<choose)-1;a>=0;a--){
		int num=0;
		for(c=0;c<choose;c++){
			if((a>>c)&1)num+=c+1;
		}

		if(num>=total){
			dp[a]=0;
			continue;
		}
		dp[a]=0;
		for(c=0;c<choose&&dp[a]==0;c++){
			if((a>>c)&1){
				continue;
			}
			int a2=(a|(1<<c));
			if(dp[a2]==0){
				dp[a]=1;
			}
		}
	}
	return dp[0];
}

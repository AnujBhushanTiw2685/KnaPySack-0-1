class Knapsack:
    def __init__(self, n, W, wt, val):
        self.n = n
        self.W = W
        self.wt = wt
        self.val = val
        
        self.reset_t() # to reset the dp after usage
        
    def reset_t(self):
        
        self.t = [[-1]*(self.W+1) for _ in range(self.n+1)]
        
    def kpRec(self, n=None , W=None):
        if n is None: n = self.n
        if W is None: W = self.W
        
        if n == 0 or W == 0:
            return 0
            
        if self.wt[n-1] <= W:
            return max(self.val[n-1]+self.kpRec(n-1, W - self.wt[n-1]), self.kpRec(n-1,W))
            
        else:
            return self.kpRec(n-1, W)
            
    def kpMem(self, n=None , W=None):
        if n is None: n = self.n
        if W is None: W = self.W
        
        if n == 0 or W == 0:
            return 0
            
        if self.t[n][W] != -1:
            return self.t[n][W]
            
        if self.wt[n-1] <= W:
            self.t[n][W] = max(self.val[n-1] + self.kpMem(n-1, W-self.wt[n-1]),
                self.kpMem(n-1,W))
        else:
            self.t[n][W] = self.kpMem(n-1, W)
            
        return self.t[n][W]
        
    
    def kpTab(self) :
        dp = [[0]*(self.W+1) for _ in range(self.n + 1)]
        
        for i in range(1, self.n + 1):
            for j in range(1, self.W + 1) :
                if self.wt[i-1] <= j:
                    dp[i][j] = max(self.val[i-1]+dp[i-1][j-self.wt[i-1]], dp[i-1][j])
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[self.n][self.W]
        



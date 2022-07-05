class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        numbers = []
        for i in range(len(accounts)):
            number = sum(accounts[i])
            numbers.append(number)
        return max(numbers)
#Time: on^2 space:on
     
                
                
        
        

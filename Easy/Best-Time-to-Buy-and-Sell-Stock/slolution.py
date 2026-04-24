class Solution:
    """
    Solution for the Best Time to Buy and Sell Stock problem.
    
    This class provides a method to find the maximum profit from buying and selling
    a stock, given an array of stock prices for each day.
    """
    
    def maxProfit(self, prices: list[int]) -> int:
        """
        Find the maximum profit from buying and selling a stock once.
        
        Approach:
        - Track the minimum price seen so far as we iterate through prices
        - For each price, calculate profit if we sell at that price
        - Update maximum profit if current profit is greater
        - Single pass algorithm, efficient and simple
        
        Constraints:
        - Can only buy once and sell once
        - Must buy before sell
        - Cannot short sell
        
        Time Complexity: O(n) where n is the length of prices array
        Space Complexity: O(1) - only using two variables
        
        Args:
            prices (list[int]): A list of integers representing stock prices on each day
            
        Returns:
            int: The maximum profit that can be made. Returns 0 if no profit can be made.
            
        Examples:
            >>> sol = Solution()
            >>> sol.maxProfit([7, 1, 5, 3, 6, 4])
            5
            >>> sol.maxProfit([7, 6, 4, 3, 1])
            0
            >>> sol.maxProfit([2, 4, 1, 7, 5, 11])
            9
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


def test_max_profit():
    """Test cases for the maxProfit method."""
    sol = Solution()
    
    # Test case 1: Standard case with profit opportunity
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5  # Buy at 1, sell at 6
    
    # Test case 2: Prices only decrease - no profit possible
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    
    # Test case 3: Buy early, sell much later
    assert sol.maxProfit([2, 4, 1, 7, 5, 11]) == 9  # Buy at 2, sell at 11
    
    # Test case 4: Single element - no transaction possible
    assert sol.maxProfit([5]) == 0
    
    # Test case 5: Empty array
    assert sol.maxProfit([]) == 0
    
    # Test case 6: Two elements with profit
    assert sol.maxProfit([2, 7]) == 5
    
    # Test case 7: Two elements with no profit
    assert sol.maxProfit([7, 2]) == 0
    
    # Test case 8: All same prices
    assert sol.maxProfit([5, 5, 5, 5]) == 0
    
    # Test case 9: Minimum at the end
    assert sol.maxProfit([3, 2, 6, 5, 0, 3]) == 4  # Buy at 2, sell at 6
    
    # Test case 10: Profit at the beginning
    assert sol.maxProfit([5, 10, 3, 7, 2, 9]) == 5  # Buy at 5, sell at 10
    
    # Test case 11: Large price difference
    assert sol.maxProfit([1, 100]) == 99
    
    # Test case 12: Multiple local maxima - should find global max
    assert sol.maxProfit([3, 8, 2, 9, 5, 10]) == 8  # Buy at 2, sell at 10
    
    # Test case 13: Profit available early, better profit later
    assert sol.maxProfit([1, 3, 2, 5]) == 4  # Buy at 1, sell at 5
    
    # Test case 14: Profit only at the end
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4  # Buy at 1, sell at 5
    
    # Test case 15: Multiple small price increases
    assert sol.maxProfit([1, 2, 3, 4, 5, 6, 7]) == 6  # Buy at 1, sell at 7
    
    # Test case 16: Large dataset with varied prices
    assert sol.maxProfit([2, 1, 2, 0, 4, 4, 3]) == 4  # Buy at 0, sell at 4
    
    # Test case 17: Negative profit scenario (all decreasing)
    assert sol.maxProfit([10, 9, 8, 7, 6, 5]) == 0
    
    # Test case 18: Single peak
    assert sol.maxProfit([1, 5, 1]) == 4
    
    # Test case 19: Two transactions pattern (but can only do one)
    assert sol.maxProfit([3, 1, 4, 2, 5]) == 4  # Buy at 1, sell at 5
    
    # Test case 20: Zero profit possible
    assert sol.maxProfit([5, 4, 3, 2, 1, 0]) == 0
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_max_profit()
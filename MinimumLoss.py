# https://www.hackerrank.com/challenges/minimum-loss/problem

def minimumLoss(prices):
    # Pair prices with their original indices
    indexed_prices = [(price, i) for i, price in enumerate(prices)]
    
    # Sort prices by value
    indexed_prices.sort()
    
    # Initialize the minimum loss to a large number
    min_loss = float('inf')
    
    # Iterate through the sorted prices to find the minimum loss
    for i in range(1, len(indexed_prices)):
        # Ensure we are buying before selling
        if indexed_prices[i][1] < indexed_prices[i - 1][1]:
            # Calculate loss
            loss = indexed_prices[i][0] - indexed_prices[i - 1][0]
            # Update minimum loss if the current loss is smaller
            if 0 < loss < min_loss:
                min_loss = loss
    
    return min_loss

n = int(input())

prices = list(map(int, input().split()))
	
print(minimumLoss(prices))
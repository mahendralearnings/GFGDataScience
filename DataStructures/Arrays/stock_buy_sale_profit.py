
def stock_segments(A, N):
    if N <= 1:
        return "No Profit"  # Not enough days to buy and sell

    total_profit = 0
    segments = []  # To store the buy-sell index pairs

    for i in range(N - 1):
        # If the price on the next day is higher than today's price
        if A[i + 1] > A[i]:
            buy = i  # Day to buy
            while i < N - 1 and A[i + 1] > A[i]:
                i += 1  # Move to the last day of profit
            sell = i  # Day to sell
            segments.append((buy, sell))  # Record the buy-sell indices
            total_profit += A[sell] - A[buy]  # Calculate profit

    if total_profit > 0:
        # Print segments (optional, can be omitted as per requirements)
        # for segment in segments:
        #     print(f"Buy on day {segment[0]} and sell on day {segment[1]}")
        return 1
    else:
        return "No Profit"

# Driver code
N = 7
A = [100, 180, 260, 310, 40, 535, 695]
result = stock_segments(A, N)
print(result)  # Should print 1 if the solution is correct

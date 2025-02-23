
def find_trailing_zeros(n: int) -> int:

        '''
            Calculate the number of trailing zeros in the factorial of a given number.

            The trailing zeros are determined by the number of times 5 is a factor in the numbers
            from 1 to n, as 2s are more abundant. This function finds all powers of 5 up to n
            and sums their counts.

            Parameters:
            n (int): The number to calculate the factorial trailing zeros for.

            Returns:
            int: The count of trailing zeros in the factorial of n.
        '''
        # Initialize result
        count = 0

        # Keep dividing n by powers of 5 and update count
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5

        return count


if __name__ == "__main__":
    # Driver code to test the function
    n = 100
    print(f"Count of trailing 0s in {n}! is {find_trailing_zeros(n)}")
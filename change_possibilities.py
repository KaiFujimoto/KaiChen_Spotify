def change_possibilities(amount, coins):
    """
    sample input: 5, [1,2,5]
    sample output: YOU'RE BROKE haha!!! jk => 4
    assumption(s) => 1. Assuming coins are positive and the amount is positive
    2. Hopefully the amount isn't like infinity, because then we'd have storage issues and time complexity issues.
    3. Overall, the goodwill of the person running my code that they will be nice. (have mercy plox)
    4. Person running my code likes notes. If not, then apologies QQ.

    """
    combinations_array = [0] * (amount + 1) # initialize an empty array to keep track of combos lol dynamic programming~~~
    combinations_array[0] = 1 # i have no idea why, it just.... it just works when I put a 1 here. I found a video about why but i'll watch it later
    for coin in coins: # iterate through each coin
        for other_amount in range(1, amount + 1): # iterate through a range between 1 and the amount plus 1 why plus 1? python's range, that's why. I treat each number I iterate through like a previous amount.
            if other_amount >= coin: # if the other_amount is bigger than the coin
                combinations_array[other_amount] += combinations_array[other_amount - coin]
                # i find the combination_array at the place and I add whatever is already there and add the combos that are already available without the coin.

    return combinations_array[amount]

print(change_possibilities(5, [1,2,5]))

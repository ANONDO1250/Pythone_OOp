sum_divisible_by_3_not_5 = sum(x for x in range(
    50, 101) if x % 3 == 0 and x % 5 != 0)
print(f"Sum of numbers between 50 and 100 divisible by 3 and not by 5: {
      sum_divisible_by_3_not_5}")

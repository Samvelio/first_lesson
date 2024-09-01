def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    calculate_average(nums) == total / count


nums = [10, 15, 20]
result = calculate_average(nums)

Print = "The average is:", result

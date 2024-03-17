def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho,
    toh unhe original list ke index ke basis par order karo.
    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    result = nums.sort()
    print(result)
    for i in range(len(nums) - 1):
        if numbers_sum(nums[i]) == numbers_sum(nums[i + 1]):
            nums.pop(nums[i])
    return nums
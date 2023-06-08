def find_duplicate(nums):
    nums_dict = {}

    for n in nums:
        if type(n) != int or n < 0:
            return False

        if nums_dict.get(n) is None:
            nums_dict[n] = 1
        else:
            nums_dict[n] += 1

    if len(nums) == len(nums_dict) or len(nums) <= 1:
        return False

    return max(nums_dict, key=nums_dict.get)

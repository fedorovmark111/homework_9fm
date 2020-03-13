import typing as tp


def find_value(nums: tp.Sequence[int], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    left,right=0,len(nums)
    if not nums:
        return False
    while left<right:
        mid=(left+right)//2
        if nums[mid]<value:
            left=mid+1
        elif nums[mid]>value:
            right=mid
        else:
            return True
    return left<len(nums) and nums[left]==value
	    
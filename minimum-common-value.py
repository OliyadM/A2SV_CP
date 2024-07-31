class Solution(object):
    def getCommon(self, nums1, nums2):
        common = None
        nums1_set = set(nums1)
        for num in nums2:
            if num in nums1_set:
                if common is None:
                    common = num
                else:
                    if common > num:
                        common = num
        if common is not None:
            return common
        else:
            return -1

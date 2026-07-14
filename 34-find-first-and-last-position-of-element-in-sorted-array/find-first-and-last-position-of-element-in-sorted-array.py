class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
       
        
        def binarySearch(left, right):
            if left > right:
                return [-1, -1]
            mid = (left + right) // 2
            if nums[mid] == target:
                start = mid
                end = mid
                m = mid + 1
                while mid != right and nums[m] == target:
                    end += 1
                    if m == right:
                        break
                    m += 1
                m = mid - 1
                while mid != left and nums[m] == target:
                    start -= 1
                    if m == left:
                        break
                    m -= 1
                return [start, end]
                    


                
                # if mid != right:
                #     m = mid+1
                #     while nums[m] == target:
                #         m += 1
                #     return [mid, mid+1]
                #     elif nums[mid-1] == target:
                #         return [mid-1, mid]
                #     else:
                #         return [mid, mid]
                # else:
                #         return [mid, mid]
            elif nums[mid] > target:
                return binarySearch(left, mid-1)
            else:
                return binarySearch(mid+1, right)
        
        return binarySearch(0, len(nums) - 1)

        
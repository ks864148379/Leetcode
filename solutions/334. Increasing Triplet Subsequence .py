"""
 Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity. 


"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3 :
            return False
        dp1 = [2**32 for x in range(len(nums))]
        dp2 = [-1 for x in range(len(nums))]
        mi = nums[0]
        ma = nums[-1]
        for i in range(1,len(nums)) :
            if nums[i] > mi :
                dp1[i] = mi
            mi = min(mi,nums[i])
        for i in range(len(nums)-2,-1,-1) :
            if nums[i] < ma :
                dp2[i] = ma
            ma = max(ma,nums[i])
        
        for i in range(1,len(nums)-1) :
            if dp1[i] != 2**32 and dp2[i] != -1 :
                return True
        return False
"""
上面的解法不好，On的空间复杂度
bool increasingTriplet(vector<int>& nums) {
    int c1 = INT_MAX, c2 = INT_MAX;
    for (int x : nums) {
        if (x <= c1) {
            c1 = x;           // c1 is min seen so far (it's a candidate for 1st element)
        } else if (x <= c2) { // here when x > c1, i.e. x might be either c2 or c3
            c2 = x;           // x is better than the current c2, store it
        } else {              // here when we have/had c1 < c2 already and x > c2
            return true;      // the increasing subsequence of 3 elements exists
        }
    }
    return false;
}
这个方法是O1复杂度空间

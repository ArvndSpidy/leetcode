"""
Revision number: 1

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Input: height = [1,1]
Output: 1

Notes:
Take a left pointer to the complete left and right pointer to the complete right. Take the minumum height of the both and the width which is right minus left (x-axis) and multiply to get the area. if the value in left pointer is less than value in right pointer, move the left pointer and vice versa.
traverse until both the pointers meet.

Time Complexit: O(n)
we iterate the list only once.
Space Complexity:O(1)

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            max_area = max(max_area, length*width)
            if height[l] >height[r]:
                r -= 1
            elif height[r] > height[l]:
                l += 1
            else:
                l += 1
                r -= 1
        return max_area

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))

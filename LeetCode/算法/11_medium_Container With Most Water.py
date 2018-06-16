'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

# 暴力破解
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        lens = len(height)
        i = 0
        while i < lens - 1:
            j = i + 1
            while j < lens:
                tmp = (j-i)*min(height[i],height[j])
                if tmp > area:
                    area = tmp
                j += 1
            i += 1
        return area
 


# 双指针法
# 初始一个放左边一个放右边，将较短的往内侧移动，这样虽然宽减小但高可能增加，终止条件为左侧指针等于右侧指针 
class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            maxarea = max(maxarea,min(height[l],height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea

# test 
h = [28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,561,772,271,178,455,44]
test = Solution2()
res = test.maxArea(h)
print(res)
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate the amount of water that can be trapped between the bars.

        Args:
            height (List[int]): A list of non-negative integers representing the height of each bar.

        Returns:
            int: The total amount of water that can be trapped.

        Example:
            Input: [0,1,0,2,1,0,1,3,2,1,2,1]
            Output: 6
            Explanation: The above elevation map (black section) is represented by the array [0,1,0,2,1,0,1,3,2,1,2,1].
                         In this case, 6 units of rainwater (blue section) are being trapped.
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0
        # Iterate the height array
        while left < right:
            if left_max < right_max:
                left += 1
                # If the current height is less than the left_max, then it can trap some water
                if left_max > height[left]:
                    res += left_max - height[left]
                # if the current height is greater than the left_max, then update the left_max
                else:
                    left_max = height[left]
            else:
                right -= 1
                # If the current height is less than the right_max, then it can trap some water
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
        return res
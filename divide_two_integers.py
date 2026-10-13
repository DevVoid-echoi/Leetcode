"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Hằng số giới hạn 32-bit signed integer
        MAX_INT = 2147483647      # 2^31 - 1
        MIN_INT = -2147483648     # -2^31
        
        # Xử lý trường hợp tràn số đặc biệt
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Xác định dấu của kết quả (dương hay âm)
        # Nếu chỉ có 1 số âm thì kết quả âm, còn lại là dương
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Chuyển cả 2 về số dương để dễ tính toán bằng bit shift
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        res = 0
        
        # Trừ dần theo lũy thừa của 2 (bit shifting)
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            # Tìm bội số lớn nhất dạng dvs * 2^k mà vẫn nhỏ hơn hoặc bằng dvd hiện tại
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            dvd -= temp
            res += multiple
            
        # Gắn lại dấu cho kết quả
        if negative:
            res = -res
            
        # Đảm bảo kết quả nằm trong khoảng giới hạn 32-bit
        return max(MIN_INT, min(MAX_INT, res))
            
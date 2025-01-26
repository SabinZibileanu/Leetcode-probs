class Solution:

    def power_of_2_sum(self, n: int) -> int:
        sum_p2 = 0

        while n != 0:
            sum_p2 += (n % 10) ** 2
            n //= 10
        
        return sum_p2

    def isHappy(self, n: int) -> bool:
        ok = True
        duplicates_check = []

        while ok:
            
            p2_sum = self.power_of_2_sum(n)
            if p2_sum not in duplicates_check:
                if p2_sum == 1:
                    break
                
                else:
                    duplicates_check.append(p2_sum)
                    n = p2_sum

            else:
                ok = False

        return ok


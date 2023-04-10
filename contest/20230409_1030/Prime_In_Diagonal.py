class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True
        d = []
        for i in range(len(nums)):
            one, two = i , -(i+1)
            if one != two :
                if is_prime(num=nums[i][one]) == True:
                    d.append(nums[i][one])
                if is_prime(num=nums[i][two]) == True:
                    d.append(nums[i][two])
        if len(d) == 0:
            return 0
        else :
            return max(d)
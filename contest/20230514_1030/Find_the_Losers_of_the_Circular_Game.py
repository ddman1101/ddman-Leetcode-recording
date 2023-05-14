class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        num = [1]
        max_times = n - 1
        temp_list = list(range(1, n+1))

        temp_num = 0
        for i in range(max_times):
            temp_num = ((k*(i+1)+ temp_num) % n)
            if temp_list[temp_num] not in num:
                num.append(temp_list[temp_num])
            else:
                break

        for j in range(len(num)):
            temp_list.remove(num[j])
            
        return temp_list
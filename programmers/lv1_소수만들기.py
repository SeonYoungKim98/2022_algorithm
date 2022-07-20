from itertools import combinations 

def solution(nums):
    answer = 0

    all_nums = list(map(sum , combinations(nums, 3)))
    
    for i in all_nums : 
        flag = True #소수인지 체크
        
        sum1 = i
        
        for j in range(2, sum1): 
            if i % j == 0 :
                flag = False 
        
        if flag == True : 
            answer += 1
            
    return answer

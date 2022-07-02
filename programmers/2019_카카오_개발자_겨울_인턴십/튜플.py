def solution(s):
    
    s = s[2 : -2]  # {{  }} 제거 
    s = s.replace('},{', ',') # },{ 제거
    answer = s.split(',') #s의 수만 들어있는 list
    
    countSet = []
    for i in answer : 
        if i not in countSet : 
            countSet.append(i) #리스트 내 원소 갯수 세기  - 1, 2, 3, 4
    #set을 쓰지 않은 이유 : set은 순서 유지하지 않고  값이 들어가므로, 아래 코드의 index 계산을 해줄 수 없어서 for문으로 돌림.
        
    countNum = []  
    for i in countSet :
        countNum.append(answer.count(i)) #3  4   2   1 
    
    finalAnswer = []
    for i in range(len(countSet)) : 
        maxNumIndex = countNum.index(max(countNum)) #현재 가장 큰 count인 수의 index 찾기 
        
        finalAnswer.append(int(countSet[maxNumIndex]))
        countNum[maxNumIndex] = -1  #maxNumber to -1
        
            
    return finalAnswer

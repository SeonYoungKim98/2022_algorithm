def solution(s):
    zeroCount, transCount = 0 , 0 #0갯수, 변환횟수
    while True:
        if s == "i" : 
            return [ transCount, zeroCount ]
    
        zeroCount += s.count("0") #0 갯수 더하기
        s = bin(s.count("1"))[2:] #0제거 후 길이로 이진수만들기
        transCount += 1 #변환횟수 1 증가

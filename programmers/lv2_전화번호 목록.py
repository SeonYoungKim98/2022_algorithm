def solution(phone_book):
    hash = {}
    
    for phoneNumber in phone_book : 
        hash[phoneNumber] = 1
        
    for phoneNumber in phone_book : 
        word= '' #접두어
        for i in phoneNumber : 
            word += i  #접두어에 하나씩 붙이기
            if word in hash and word != phoneNumber : #접두어가 해시 안에 존재하고, 
                return False
    
    return True

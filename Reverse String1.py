def rev_str(str):    
    word1 = ""     
    for i in str:  
        word1 = i+word1  
    return word1      
str = "1234abcd"
print("The Given String is:",(str))
print("The Reverse String is:",rev_str(str))



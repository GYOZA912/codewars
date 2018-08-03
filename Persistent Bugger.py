'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 '''

def persistence(n):
    if len(str(n))==1:
        return 0
    else:
        #print(n)
        char=''.join(str(n))
        count=0
        while True:
            mul=1
            for i in range(len(char)):
                #print(char[i])
                mul=mul*int(char[i])
                #print(mul)
            count=count+1
            #print(count)
            if len(str(mul))==1:
                break
            else:
                char=''.join(str(mul))
                #print(char)
        return count

    

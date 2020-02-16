'''N students take K apples and distribute them among each other evenly. The
remaining (На английском языке что бы Вы научились понимать the undivisible) part remains in the basket. How many apples will
each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for
the questions above. (На английском языке что бы Вы научились понимать Each N student will take K apples, and remains X)
'''
N = int(input('apples'))
K = int(input('student'))
print('Each student will get', N // K)
print('remains in the basket', N % K) 



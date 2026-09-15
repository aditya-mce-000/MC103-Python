n = 10
a = 0
b = 1
print(a, end =" ")
print(b, end =" ")

for i in range(n):
    temp = b 
    b= a + b
    a = temp
    print(b, end = " ")
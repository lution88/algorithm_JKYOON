number = int(input())

num = [0, 1]
for i in range(number):
    num.append(num[i] + num[i+1])
    
print(num[number])
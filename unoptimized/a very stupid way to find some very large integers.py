import math

def A(num):
    numbers = list()
    i = 2
    while len(numbers) != num:
        flag = False
        for x in range(2, i):
            if i % x == 0:
                flag = True
                break
        
        if not flag:
            reverse = int(str(i)[::-1])
            x = reverse ** 0.5
            if math.floor(x) * math.floor(x) == reverse:
                numbers.append(i)
        
        i += 1
    
    return numbers[-1]

def B(num):
    lists = [[1, 1]]
    while len(lists) != num:
        new_list = list()
        for i in range(len(lists[-1]) - 1):
            new_list.append(lists[-1][i] + lists[-1][i + 1])
        new_list = [1] + new_list + [1]
        lists.append(new_list)
    return max(lists[-1])

def C(num):
    numbers = list()
    i = 2
    while len(numbers) != num:
        flag = False
        for x in range(2, i):
            if i % x == 0:
                flag = True
                break
        
        if not flag:
            a = i + 1
            if a != 0 and a & (a - 1) == 0:
                numbers.append(i)
        
        i += 1
    
    return numbers[-1]

def D(num):
    numbers = list()
    i = 1
    while len(numbers) != num:
        if all(x in '10' for x in str(i)):
            numbers.append(i)
        i += 1
    return numbers[-1]

print(A(14357) % 1639049501)
print(B(10000) % 39481900)
print(C(13) % 74930667869)
print(D(100000) % 90213568157) 
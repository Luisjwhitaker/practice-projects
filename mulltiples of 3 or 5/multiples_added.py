def solution(number):
    list=[]
    answer = 0
    for i in range(1,number):
        if i % 3 == 0:
            list.append(i)
        elif i % 5 ==0:
            list.append(i)
    for i in list:
        answer = answer+i
    return answer

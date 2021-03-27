def fizz_buzz(fizz_number, buzz_number, ran=100):
    for i in range(1,ran+1):
        answer= []
        value=0
        if i % fizz_number == 0:
            answer += ['fizz ']
            value=1
        if i % buzz_number == 0:
            answer += ['buzz']
            value=1
        if value == 0:
            answer += [i]
        print(answer)

fizz_buzz(3,5,50)

def fizz_buzz(fizz_number, buzz_number, game_range=100):
    list_return = []
    for i in range(1,game_range+1):
        answer= ''
        value=0
        if i % fizz_number == 0:
            answer += 'fizz '
            value=1
        if i % buzz_number == 0:
            answer += 'buzz'
            value=1
        if value == 0:
            answer += str(i)
        list_return+=[answer]
    return list_return

print(fizz_buzz(3,5,50))

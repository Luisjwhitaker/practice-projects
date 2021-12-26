def solution(s):
    answer = []
    if len(s)%2 != 0:
        s += '_'
    for i in range(0,len(s),2):
        answer += [s[i:i+2]]
    return answer

print(solution('helloworlds'))

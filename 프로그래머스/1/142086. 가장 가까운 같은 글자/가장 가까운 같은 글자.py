# 2월 27일 하

def solution(s):
    answer = []
    # 앞서 나온 글자 저장
    c = {}

    for i in range(len(s)):
        if s[i] not in c:
            c[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - c[s[i]])
            c[s[i]] = i

    return answer
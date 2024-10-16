def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(i, play)]
        else:
            dic1[genre].append((i, play))
        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
  
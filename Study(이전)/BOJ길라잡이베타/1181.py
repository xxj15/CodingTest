# 단어정렬 (실5)

N = int(input())
words = [[] for _ in range(51)]

for _ in range(N):
  word = input()
  idx = len(word)
  if word not in words[idx]:
    words[idx].append(word)


for word_list in words:
  word_list.sort()
  if word_list:
    for word in word_list:
      print(word)

# 정렬을 이용해 한 번에 간단하게 풀이할 수도 있다.
# import sys

# N = int(sys.stdin.readline())
# words = {sys.stdin.readline().strip() for _ in range(N)}  # set으로 중복 제거
# for w in sorted(words, key=lambda s: (len(s), s)):        # 길이→사전순
#     print(w)

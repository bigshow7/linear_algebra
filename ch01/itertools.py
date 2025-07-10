#조합과 순열을 연습하는 코드
#7개의 곡 중 3개를 뽑아 재생순서를 만들어야 함

import itertools

songs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#7개 중 3곡을 뽑는 조합
combinations = list(itertools.combinations(songs, 3))
print(f"7곡 중 3곡을 뽑는 조합의 수: {len(combinations)}가지")

#7개 중 3곡을 뽑아 재생순서까지 만드는 순열
permutations = list(itertools.permutations(songs, 3))
print(f"가능한 재생목록 : {permutations}")

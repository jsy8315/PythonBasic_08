# 주요 라이브러리의 문법과 유의점

# eval() 함수
result = eval("(3+5)*7")
print(result)

# sorted() 함수
result = sorted([9,1,8,5,4])
print(result)

result = sorted([9,1,8,5,4], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

# 리스트 함수는 sort()함수를 내장함
data = [9,1,8,5,4]
data.sort()
print(data)

# itertools

# 순열permutation
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print("순열: ", result)

# 조합combination
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print("조합: ", result)

# 중복 순열product
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print("중복순열: ", result)

# 중복 조합combinations_with_replacement
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2))
print("중복조합: ", result)

# heapq

# counter, 등장 횟수를 세는 기능
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

# math 라이브러리
# 최대공약수
import math
def lcm(a,b):
  return a*b //math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21,14)) #최대공약수계산
print(lcm(21,14)) #최소 공배수 계산
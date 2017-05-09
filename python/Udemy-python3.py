## lesson5
print('spam eggs')
print('doesn\'t')
print("doesn't")
s = 'First line \nSecond line'
print(s)

## lesson6
print('C:\some\name')
### rawで出力
print(r'C:\some\name')

### 三連引用符
print('''
Usage:
    -h help
    ''')
print('''\
Usage:
    -h help
''')


## lesson7
### index
word = 'Python'
print(word[0] + word[5])
print(word[-2] , word[-4])

### slice
print(word[0:2])
### indexは範囲外はエラーとなり、sliceはエラーにならない
print(word[4:53])

### 文字列の長さを知る
s = "sdfsafdasjdkflajsdl;fkjasldkfjasl;dkfjasld"
print(len(s))

## lesson8
### list
squares = [1, 4, 9, 16, 25]
print(squares[0])
print(squares[1])
print(squares[3])
print(squares[-2])
print(squares[-3:])
### リスト全体のコピー
print(squares[:])
### リストの追加(これだけでは変数の中身は変わらない)
print(squares + [36, 49, 64, 81, 100])

squares = squares + [36, 49, 64, 81, 100]
print(squares)

cubes = [1, 8, 27, 65, 125]
print(cubes)
print(4 ** 3)
print(cubes[3])
cubes[3] = 4 ** 3
print(cubes)
print(6 ** 3)
cubes.append(6 ** 3)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[2:5])
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
print(letters[:])
letters[:] = []
print(letters)
print(len(letters))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(len(letters))
# len()関数は文字数を数えているわけではなく、リストの数を数えている
letters = ['aa', 'bb', 'c', 'd', 'e', 'f', 'g']
print(len(letters))
# ネスト/入れ子
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a,n]
print(x)
print(x[0])
print(x[1])
# bを出力する
print(x[0][1])
# while文とフィボナッチ数列
# 1, 1, 2, 3, 5, 8, 13
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

i = 256 * 256
print('The value of i is', i)

import sys
print(sys.version)
a, b = 0, 1
while b < 1000:
    print(b, end=",")
    a, b = b, a+b

# if statement
x = -1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

a = 1
b = 2
c = 3

a < b
a > b
a == b
b < c
a < b < c
a < b and b < c
a < b or b < c
not a < b
not a > b
words = ['cat', 'window', 'defenestrate']
# pythonのfor文は for-in statement

for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)

# range関数
for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)
    
for i in range(0, 10, 3):
    print(i)

print(list(range(5)))

# break

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# continue

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        break
    print("Found a number", num)

# 関数

def fib(n):
    """Print a Fibonacci series up to n. """
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a + b
    print()

fib(2000)
fib
f = fib
f(100)

def fib2(n):
    """Return a list contining the fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)


# 関数、引数

def ask_ok(prompt, retries=4, complaint='Yes or no , please !'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
# 関数の引数
## デフォルト値は関数定義時にきまっている
i = 5
def f(arg=i):
    print(arg)

i = 6
f()

## デフォルト値は関数の実行時の初回しか評価されない

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# キーワード引数
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sourted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

# 任意引数、可変長引数、可変個引数

def concat(*args, sep="/"):
    return sep.join(args)

# 引数リストのアンパック


# ディクショナリのアンパック
    

# lamda
## 動的に関数を作成する
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print(f(0))
print(f(1))
print(f(2))
print(f(3))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# リスト
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2, -1)
print(a)
a.remove(333)
print(a)
# aのリストそのものを変更する
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)

# スタック(後入れ先出し)
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)

# キュー(先入れ先だし)
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)


# リスト内包表記
## 通常のリスト作成
squares = []

for x in range(10):
    squares.append(x**2)
print(squares)

## リスト内包表記
squares2 = [ x**2 for x in range(10)]
print(squares2)

combs = []

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

combs2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs2)

vec = [-4, -2, 0, 2, 4]

vec2 = [ x*2 for x in vec]
print(vec2)

vec3 = [x for x in vec if x >= 0]
print(vec3)

vec4 = [abs(x) for x in vec]
print(vec4)

freshfruit = [' banana', ' loganberry ', 'passion fruit ']
freshfruit2 = [x.strip() for x in freshfruit]
print(freshfruit2)

print([(x, x**2) for x in range(6)])
print([x**2 for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print(vec)

print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1,6)])

# matrix
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))

# del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)

# tuple
a = [1,2,3]
b = (1,2,3)

print(a[0])
print(b[0])

a[0] = 0
print(a)

# tupleは値を変更できない
# カンマ区切りで変数に代入するとタプル型になる
t = 12345, 54321, 'hello!'
print(t)

# 1個の値をもつタプルを作成するには、カンマで区切る
t = 1234
print(type(t))

t = 1234,
print(type(t))

t = 12345, 54321, 'hello!'
u = t, (1,2,3,4,5,)
v = t, 1,2,3,4,5,
print(t, u, v)

v = ([1,2,3], [3,2,1])
print(v[0])

empty = ()
print(empty)


t = 12345, 54321, 'hello!'
x, y, z = t
print(x,y,z)


# 集合 Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)

# 空の集合を作る
empty = set()
print(type(empty))

# 集合演算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a - b)
# 和
print(a|b)
# 積
print(a&b)
# 除
print(a^b)

# set 内包
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# dictionary
tel = {'jack': 4098, 'sape': 4139}
print(tel)

# 値の追加
tel['guido'] = 4127
print(tel)

# 値の削除はdel文
del tel['sape']
print(tel)

tel['irv'] = 4127

# keyだけを抜き出す
print(tel.keys())

# dicからlistへ
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)

# 値をだけ抜き出す
print(tel.values())
print(list(tel.values()))

# 辞書の初期化
tel = {}
print(tel)
# 辞書のコンストラクタ
print(dict())

# リストとタプルから辞書を生成する
print(dict([('sape', 1111), ('guido', 4127), ('jack', 4098)]))

# 辞書内包表記
print({x: x**2 for x in (2,4,6)})

# 辞書の生成　キーワード引数
tel = dict(sape=1111, guido=4127, jack=4098)
print(tel)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)


# ループ技法
# リストをfor文で回す時にインデックスの値をとりたい
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 2つのリストを組み合わせて使う
questions = ['name', 'quest', 'fovorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# シーケンスを逆方向にループ
for i in reversed(range(1, 10, 2)):
    print(i)


# sort
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filterd_data = []
for value in raw_data:
    if not math.isnan(value):
        filterd_data.append(value)

print(filterd_data)


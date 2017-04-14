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
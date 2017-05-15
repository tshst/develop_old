print('We are the {} who sya "{}"'.format('knights', 'Ni'))

# formatの引数を数字で指定する

print('{0} and {1}'.format('spam', 'eggs'))

# 番号を入れ替える
print('{1} and {0}'.format('spam', 'eggs'))

# キーワード引数
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# 小数点のフォーマットも指定できる
import math

print('The value of PI is approximately {0:.3f}'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))



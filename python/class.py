class MyClass:
    """A simple example class """
    i = 12345

    # クラスの中の関数はメソッドと呼ぶ
    # クラスの中でメソッドを定義するときには、引数にselfを指定する
    def f(self):
        return "hello world"

if __name__ == '__main__':
    x = MyClass()
    y = MyClass()
    #　同じクラスを変数に代入しても、それぞれ別物として扱うことができるのがメリット
    # yのiの値を変更してもxのiには影響しない
    y.i = 54321
    print(x.i)
    print(y.i)
    print(x.f())
    print(y.f())

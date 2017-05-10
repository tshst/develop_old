class MyClass:
    """A simple example class """
    # インスタンス化された時にだけ呼ばれる初期化処理
    # オブジェクト自身(ここではMyClass)のことをselfという
    def __init__(self):
        # 初期化処理の時にdataという空のリストを作成する
        self.data = []

    i = 12345

    # クラスの中の関数はメソッドと呼ぶ
    # クラスの中でメソッドを定義するときには、引数にselfを指定する
    def f(self):
        return "hello world"

class Complex:
    # 初期化の際に変数を指定できる
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

if __name__ == '__main__':
    x = MyClass()
    # インスタンス生成後に変数を追加することはできる
    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter*2
    # 追加した変数に対して、変更を加えることもできる
    print(x.counter)
    # 不要になったら削除することもできる
    del x.counter

    # インスタンス生成時にdataという空のリストが作成される
    x.data.append('a')
    print(x.data)
    y = MyClass()
    #　同じクラスを変数に代入しても、それぞれ別物として扱うことができるのがメリット
    # yのiの値を変更してもxのiには影響しない
    y.i = 54321
    print(y.i)

    # インスタンス化の際に値を渡すことができる
    z = Complex(5.0, -4.5)
    print(z.r)
    print(z.i)

    

# メソッド

## `@classmethod` - クラスメソッド

### `main.py`

``` py
class MyClass:

    a = 1000

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    @classmethod
    def myClassMethod(cls, arg1):
        print("call myClassMethod", arg1, cls.a)

if __name__ == "__main__":
    instance = MyClass(100, 200)
    instance.myMethod(1)
    MyClass.myClassMethod(10)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 100 200
call myClassMethod 10 1000
```

### 解説

* `@classmethod` デコレータによってクラスメソッド（クラスに定義するメソッド）を定義できる
* クラスメソッドは第1引数にクラスインスタンス（ `cls` ）を受け取り、クラス変数（ `a` ）にアクセスできる
* `MyClass.myClassMethod(10)` のようにクラス名を指定して呼び出す

> クラスメソッドに対して、通常のメソッドのことをインスタンスメソッドと呼ぶこともあります。インスタンスメソッドはクラスから生成したインスタンスに対して呼び出すメソッドで、クラスメソッドはクラスインスタンス（クラスそのもの）に対して呼び出すメソッドです。

---

## `@staticmethod` - スタティックメソッド

### `main.py`

``` py
class MyClass:

    a = 1000

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    @classmethod
    def myClassMethod(cls, arg1):
        print("call myClassMethod", arg1, cls.a)

    @staticmethod
    def myStaticMethod(arg1):
        print("call myStaticMethod", arg1)

if __name__ == "__main__":
    instance = MyClass(100, 200)
    instance.myMethod(1)
    MyClass.myClassMethod(10)
    MyClass.myStaticMethod(100)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 100 200
call myClassMethod 10 1000
call myStaticMethod 100
```

### 解説

* Pythonには `@classmethod` デコレータとよく似た `@staticmethod` デコレータが用意されている
* スタティックメソッドはクラス変数にアクセスできない
* 引数だけで戻り値が決定するようなシンプルなメソッドを表現できる

> スタティックメソッドもクラスメソッドと同様に `MyClass.myStaticMethod(100)` のようにクラスに対して呼び出します。

---

## 演習

* [エクササイズ - メソッド](../ex/04_method_ex.md)

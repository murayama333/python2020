# クラスとインスタンス 

## クラスとインスタンス

### `main.py`

``` py
class MyClass:
    pass

if __name__ == "__main__":
    instance = MyClass()
    print(instance)
```

### 実行結果

``` 
$ python main.py
<__main__.MyClass object at 0x107c54040>
```

### 解説

* `class` キーワードでクラスを定義する
* クラス名は先頭を大文字のキャメルケースで付けることが多い
* 通常、定義したクラスはインスタンス化 `MyClass()` して使う

> 1つのクラスからインスタンスは複数生成できます。

---

## メソッド

### `main.py`

``` py
class MyClass:
    def myMethod(self, arg1):
        print("call myMethod", arg1)


if __name__ == "__main__":
    instance = MyClass()
    instance.myMethod(1)
```

### 実行結果

``` 
$ python main.py
call myMethod 1
```

### 解説

* メソッドとはクラスの中に定義した関数のこと
* 通常のメソッドはインスタンスに対して呼び出す
* メソッドは第1引数に `self` を受け取る

> 第1引数の `self` にはインスタンス自身の参照が代入されます。引数の名前には `self` という名前を付けることが一般的です。

---

## データ属性

### `main.py`

``` py
class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)

if __name__ == "__main__":
    instance = MyClass()
    instance.myMethod(1)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 10 20
```

### 解説

* データ属性とはクラスの中に定義した変数のこと
* メソッドからデータ属性にアクセスできる
* メソッドの中では `self` キーワードでデータ属性にアクセスする

> データ属性（ `Data Attribute` ）は、インスタンス変数、フィールド、プロパティなどと呼ぶこともあります。

---

## `__init__` メソッド

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)

if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.myMethod(1)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 10 20
```

### 解説

* `__init__` メソッドはインスタンス生成時に呼び出される特殊なメソッド
* `__init__` メソッドはコンストラクタと呼ぶこともある
* `__init__` メソッドは引数で受け取ったデータでデータ属性を初期化する

> インスタンス生成時に `MyClass(10, 20)` のように引数を指定します。

---

## 演習

* [エクササイズ - クラスとインスタンス](../ex/01_class_ex.md)

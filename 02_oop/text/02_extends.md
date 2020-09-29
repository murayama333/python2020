# 継承

## 継承

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)

class MySubClass(MyClass):
    def myMethod2(self):
        print("call myMethod2")

if __name__ == "__main__":
    instance = MySubClass(10, 20)
    instance.myMethod(1)
    instance.myMethod2()
```

### 実行結果

``` 
$ python main.py
call myMethod 1 10 20
call myMethod2
```

### 解説

* `class MySubClass(MyClass)` と記述することで `MyClass` を継承した `MySubClass` クラスを定義できる
* 継承元のクラスを親クラスやスーパークラス、継承して作成する新たなクラスを子クラスやサブクラスなどと呼ぶ
* サブクラスではスーパークラスのメンバ（データ属性やメソッド）を再利用できる

> Pythonは多重継承をサポートしています。カンマで区切って複数のスーパークラスを指定できます。

---

## メソッドのオーバーライド

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)

class MySubClass(MyClass):
    def myMethod(self, arg1):
        print("call MySubClass#myMethod", arg1, self.x, self.y)

    def myMethod2(self):
        print("call myMethod2")

if __name__ == "__main__":
    instance = MySubClass(10, 20)
    instance.myMethod(1)
    instance.myMethod2()
```

### 実行結果

``` 
$ python main.py
call MySubClass#myMethod 1 10 20
call myMethod2
```

### 解説

* スーパークラスのメソッドをサブクラスで再定義することをオーバーライドと呼ぶ
* オーバーライドによって既存のメソッドの処理を上書きできる
* 新たなクラスを作成して継承を利用することで、既存のクラスを修正することなく処理を拡張できる

---

## `super()` 呼び出し

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)

class MySubClass(MyClass):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def myMethod(self, arg1):
        print("call MySubClass#myMethod", arg1, self.x, self.y)

    def myMethod2(self):
        print("call myMethod2")

if __name__ == "__main__":
    instance = MySubClass(10, 20, 30)
    instance.myMethod(1)
    instance.myMethod2()
```

### 実行結果

``` 
$ python main.py
call MySubClass#myMethod 1 10 20
call myMethod2
```

### 解説

* `super()` 呼び出しによってスーパークラスのメンバにアクセスできる
* `__init__` メソッドで親クラスの `__init__` メソッドを呼び出すことができる
* `__init__` メソッドは所属するクラスに定義したデータ属性の初期化を行う

---

## 演習

* [エクササイズ - 継承](../ex/02_extends_ex.md)

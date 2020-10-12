# データ属性とカプセル化

## データ属性

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
    instance.x = 100
    instance.y = 200
    instance.myMethod(1)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 100 200
```

### 解説

* データ属性はインスタンスの持つ変数
* インスタンスメソッド中では `self` 変数からアクセスできる
* 外部のプログラムからもインスタンスの持つデータ属性にアクセスできる

> 一般的に、オブジェクト指向プログラミングにおいて、外部からアクセス可能な状態（データ属性）は好ましくありません。カプセル化というアプローチに従って、メソッド経由でデータ属性にアクセスするようにします。

---

## データ属性のマングリング

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.__x = 100
    instance.__y = 200
    instance.myMethod(1)

    instance._MyClass__x = 100
    instance._MyClass__y = 200
    instance.myMethod(1)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 10 20
call myMethod 1 100 200
```

### 解説

* Pythonのデータ属性は名前の先頭に `__` を付けることで属性名をマングリング（ `Mangling` ）できる
* マングリング（切り刻むという意味）とは外部から名前を推測しにくいように変換すること
* マングリングによって外部プログラムからの直接的なアクセスを禁止できるが、変換ルールに従えばアクセスできる

> マングリングされたデータ属性は、非公開データ属性を意味します。特別な理由がない限り、外部からアクセスしないようにします。

---

## Getter/Setter

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.set_x(100)
    instance.set_y(200)
    instance.myMethod(1)
    print(instance.get_x())
    print(instance.get_y())
```

### 実行結果

``` 
$ python main.py
call myMethod 1 100 200
100
200
```

### 解説

* データ属性にアクセスするためのメソッドをGetter/Setterなどと呼ぶ
* Getterメソッドはデータ属性の値を戻り値として返し、Setterメソッドは引数で受け取ったデータをデータ属性に代入する
* `get_` や `set_` のようにシンプルにネーミングすることが多い

> たとえばSetterメソッドの引数を `if` 文でチェックしたりすることで、データ属性への不正な代入を禁止することできます。またSetterメソッド（Getterメソッド）は提供せずに、Getterメソッド（Setterメソッド）だけを提供するといった実装も可能です。このようにデータ属性への不正なアクセスを保護することがGetter/Setterの目的です。このような考え方をカプセル化と呼びます。

---

## プロパティ

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.x = 100
    instance.y = 200
    instance.myMethod(1)
    print(instance.x)
    print(instance.y)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 100 200
100
200
```

### 解説

* Getter/Setterメソッドを `property` メソッドによってプロパティに置き換えることができる
* 外部のプログラムからは `instance.x` や `instance.y` のようにアクセスできる
* プロパティによって「公開しているデータ属性」を表現できる。

> デフォルトのデータ属性には、公開されているデータ属性なのか、非公開のデータ属性なのか意図が伝わりにくいという問題があります。プロパティによって、公開されているデータ属性であることを明確にできます。

---

## `@property` デコレータ

### `main.py`

``` py
class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.x = 100
    instance.y = 200
    instance.myMethod(1)
    print(instance.x)
    print(instance.y)
```

### 実行結果

``` 
$ python main.py
call myMethod 1 100 200
100
200
```

### 解説

* Pythonにはプログラムを拡張するデコレータという仕組みがある
* `@property` によってプロパティ（Getter）を簡単に表現できる
* プロパティ（Setter）が必要な場合は`@x.setter`のようにプロパティ名をデコレータに使う

---

## 演習

* [エクササイズ - データ属性とカプセル化](../ex/03_capsule_ex.md)

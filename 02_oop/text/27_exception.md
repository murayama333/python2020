# 例外処理

## 例外処理

### `ex1.py`

``` py
x = int(input("X: "))
y = int(input("Y: "))
try:
    z = x / y
    print(z)
except:
    print("except")
```

### 実行結果

``` 
$ python ex1.py 
X: 2
Y: 0
except
```

> `y` に `0` を代入すると例外が発生します。

### 解説

* Pythonでは0による除算が発生した場合、 `ZeroDivisionError` 例外が発生する
* プログラムの中で発生した例外は `try - except` 構文で処理できる
* `try` ブロック内で例外が発生した場合、処理は `except` ブロックに移る

---

### `ex2.py`

``` py
x = int(input("X: "))
y = int(input("Y: "))
try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
```

### 実行結果

``` 
$ python ex2.py
X: 2
Y: 0
ZeroDivisionError division by zero
```

### 解説

* `except` ブロックには捕捉の対象とする例外の型を指定できる
* `except ZeroDivisionError as e:` と記述した場合、 `ZeroDivisionError` 例外のみを捕捉し、発生した例外オブジェクトを変数 `e` に代入できる
* `except` ブロックでは例外オブジェクトの代入されている変数 `e` を使って例外情報にアクセスできる

---

### `ex3.py`

``` py
x = int(input("X: "))
y = int(input("Y: "))
try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
else:
    print("else")
finally:
    print("finally")
```

### 実行結果

``` 
$ python ex3.py
X: 2
Y: 0
ZeroDivisionError division by zero
finally
```

### 解説

* `try - except` 構文には `else` ブロック、 `finally` ブロックを追記できる
* `else` ブロックはtryブロック内で例外が発生しなかった場合（正常時）のみ実行される
* `finally` ブロックは例外発生の有無に関わらず必ず実行される

> `try - finally` のように `except` ブロックを省略することもできます。

---

### `ex4.py`

``` py
x_list = [int(x) for x in input("X: ").split(" ")]
y_list = [int(y) for y in input("Y: ").split(" ")]
try:
    for i in range(len(x_list)):
        z = x_list[i] / y_list[i]
        print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
except IndexError as e:
    print("IndexError", e)
```

### 実行結果

``` 
$ python ex4.py
X: 10 20 30
Y: 1 2
10.0
10.0
IndexError list index out of range
```

### 解説

* `except` ブロックは複数定義して、発生した例外ごとに処理を定義できる
* `except (ZeroDivisionError, IndexError) as e:` のように処理をまとめることもできる

---

### `ex5.py`

``` py
class MyError(Exception):
    pass


def check_value(value):
    if value < 0:
        raise MyError(f"Invalid value: {value}")
    return "OK"


try:
    print(check_value(1))
    print(check_value(-1))

except MyError as e:
    print(e)
```

### 実行結果

``` 
$ python ex5.py
OK
Invalid value: -1
```

### 解説

* `Exception` クラスを継承して独自の例外クラスを定義できる
* 生成した例外オブジェクトは `raise` キーワードで呼び出し元に返却できる
* `except MyError as e:` のように例外オブジェクトを捕捉できる

> `Exception` クラスにはメッセージを受け取るコンストラクタ（ `__init__` メソッド）が用意されています。そのため `MyError(f"Invalid value: {value}")` のようにインスタンスを生成できます。

---

### 参考：例外のクラス階層

https://docs.python.org/ja/3.7/library/exceptions.html#exception-hierarchy

---

## 演習

* [エクササイズ - 例外処理](../ex/27_exception_ex.md)

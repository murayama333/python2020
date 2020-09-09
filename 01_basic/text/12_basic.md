# 関数 - 関数の定義

### `def1.py`

``` python
def add(x, y):
    z = x + y
    return z

a = add(10, 20)
b = add(30, 40)
c = add(a, b)
print(c)
```

> 定義した関数は何度でも呼び出すことができます。

### 実行

``` 
$ python def1.py 
100
```

### 解説

* 足し算をする `add` 関数を定義する
* `add` 関数は引数に `x` と `y` の2つを受け取る
* `add` 関数は戻り値 `x` と `y` の加算結果を返す

#### 関数定義

* 関数を定義するにはdefキーワードを使う
* `def` キーワードの後に関数名と引数を定義する
* 関数の戻り値は `return` キーワードで指定する

``` 
def 関数名(引数):
    処理
    return 戻り値
```

> Pythonは関数の処理ブロックもインデントで表現します。引数の後に `:` を付けることを忘れないようにしてください。

---

### `def2.py`

``` python
def hello(repeat):
    for i in range(repeat):
        print("Hello")

hello(5)
```

> 戻り値を返さない関数を定義できます。

### 実行

``` 
$ python def2.py
Hello
Hello
Hello
Hello
Hello
```

### 解説

* 引数で受け取った回数 `"Hello"` と出力する `hello` 関数を定義する
* `hello` 関数の引数 `repeat` に `5` を指定して呼び出す
* `hello` 関数の戻り値はない

---

### `def3.py`

``` python
from random import randint

def random_list():
    size = randint(1, 9)
    return list(range(size))

list = random_list()
print(list)
```

> 引数を受け取らない関数を定義できます。

### 実行

``` 
$ python def3.py
[0, 1, 2, 3, 4, 5, 6, 7]
```

> 実行するたびにリストの要素数が変化します。

### 解説

* ランダムな要素数を持つリストを返却する `random_list` 関数を定義する
* `random_list` 関数は引数を受けとらない
* `hello_world` 関数は戻り値にランダムな要素数を持つリストを返す

---

### `def4.py`

``` python
def hello_world():
    print("Hello World!")

hello_world()
```

> 引数も戻り値もない関数を定義できます。

### 実行

``` 
$ python def4.py 
Hello World!
```

### 解説

* `"Hello World!"` を出力する `hello_world` 関数を定義する
* `hello_world` 関数を引数なしで呼び出す
* `hello_world` 関数の戻り値はない

---

### `def5.py`

``` python
def hello_world(upcase=False, repeat=1):
    for i in range(repeat):
        if upcase:
            print("HELLO WORLD!")
        else:
            print("Hello World!")

hello_world()
hello_world(True)
hello_world(False, 3)
```

> hello_world関数の2つの引数upcase、repeatはデフォルト値が定義されています。これにより、関数呼び出し時に引数を省略することができます。

### 実行

``` 
$ python def5.py
Hello World!
HELLO WORLD!
Hello World!
Hello World!
Hello World!
```

### 解説

* Pythonの関数は引数にデフォルト値を定義できる

---

### `def6.py`

* 再帰的に値を出力する `recursion` 関数を定義する
* `recursion` 関数の中で再度 `recursion` 関数を呼び出すことができる
* このような関数呼び出しを再帰呼び出しと呼ぶ

``` python
def recursion(x):
    if x < 10:
        print(x)
        recursion(x + 1)

recursion(1)
```

> recursion関数は再帰的な関数です。

### 実行

``` 
> python func6.py
1
2
3
4
5
6
7
8
9
```

---

### 演習

* [エクササイズ - 関数の定義](../ex/12_basic_ex.md)

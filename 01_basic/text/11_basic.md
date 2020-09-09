# 関数 - 組み込み関数

### `func1.py`

``` python
x = 3
y = -2
x2 = abs(x)
y2 = abs(y)
print(x, x2)
print(y, y2)
```

### 実行

``` 
$ python func1.py 
3 3
-2 2
```

> `print` 関数に渡している `x` や `x2` も引数です。 `print` 関数は複数の引数を受け取ることができます。

### 解説

* Pythonにはいくつかの組み込み関数が用意されている
* 関数に渡すデータを引数、関数から返却されるデータを戻り値と呼ぶ
* `abs` 関数は引数で数値を受け取り、戻り値にその絶対値を返す

---

### `func2.py`

``` python
list = [10, 20, 30]

x = sum(list)
y = max(list)
z = min(list)

print("Sum:", x)
print("Max:", y)
print("Min:", z)
```

### 実行

``` 
$ python func2.py
Sum: 60
Max: 30
Min: 10
```

### 解説

* `sum` 関数、 `max` 関数、 `min` 関数リストやタプルのようなデータを引数に受け取り、その結果を戻り値として返す

---

### `func3.py`

``` python
s1 = "10"
s2 = "3.14"
s3 = "True"

i = int(s1)
f = float(s2)
b = bool(s3)

print(type(i))
print(type(f))
print(type(b))
```

### 実行

``` 
$ python func3.py
<class 'int'>
<class 'float'>
<class 'bool'>
```

> `type` 関数は引数で受け取ったデータの型を戻り値として返します。

### 解説

* `int` 関数、 `float` 関数、 `bool` 関数、 `str` 関数など、データ型を変換する関数が用意されている

---

### `func4.py`

``` python
x = input("-->")
print(x)
```

### 実行

``` 
$ python func4.py
-->Hello
Hello
```

> プログラムを実行すると一時停止し、キーボードからの入力を受け付けます。Enterキーを押すと `input` 関数の戻り値が確定し、後続の処理が実行されます。

### 解説

* `input` 関数は標準入力を処理する

---

### `func5.py`

``` python
x = 1
print(x)

breakpoint()

x = 2
print(x)

breakpoint()

x = 3
print(x)
```

### 実行

``` 
x = 1
breakpoint()
print(x)
x = 2
print(x)
x = 3
print(x)
```

### 解説

* `breakpoint` 関数を呼び出すとデバッガ（Pdb）を起動できる

### デバッガの使い方

|キー|動作|
|:--|:--|
|l|ソースコードを表示する|
|n|次の行に進む|
|s|次の行に進む（関数呼び出し時は、関数定義に入る）|
|c|次のブレークポイントに進む|
|p|変数を表示する（ `p 変数名` のように指定する）|
|q|デバッガを終了する|

> https://docs.python.org/ja/3/library/pdb.html#debugger-commands

---

### 演習

* [エクササイズ - 組み込み関数](../ex/11_basic_ex.md)

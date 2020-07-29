# 変数と演算子

### `var1.py`

``` python
price = 200
count = 5
total = price * count
message = "TOTAL PRICE"

print(message)
print(total)
```

### 実行

``` 
$ python var1.py
TOTAL PRICE
1000
```

### 解説

* 変数には整数や文字列といったデータを代入できる
* 文字列データは `""` あるいは `''` で囲む
* 算術演算子( `+, - , *, /, %` )が利用できる

---

### `var2.py`

``` python
count = 1
count = count + 1

print(count)
```

### 実行

``` 
$ python var2.py
2
```

### 解説

* 1つのステートメントに同じ名前の変数を利用できる
* 変数の値を1増やすことをインクリメントと呼ぶ
* Pythonには `++` のインクリメント演算子は用意されていない

---

### `var3.py`

``` 
number = 10
p = number > 0
n = number < 0

print(p)
print(n)
```

### 実行

``` 
$ python var3.py
True
False
```

### 解説

* 比較演算子（ `>, >=, ==, <=, <, !=` ）によって2つの値を比較できる
* 比較演算子の評価結果は真理値型（ `True` , `False` ）となる
* 真理値型は後で学習する制御構文で利用する

> 演算子には、ここで紹介した算出演算子や比較演算子以外にも論理演算子（bool演算子）などが存在します。これらについては後述します。

### 外部リンク

* [組み込み型 - 比較](https://docs.python.org/ja/3/library/stdtypes.html#comparisons)

---

### `var4.py`

``` python
a = 1
b = "1"
c = 1.0
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

### 実行

``` 
$ python var4.py 
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

### 解説

* `type` 関数によって変数に格納されているデータのデータ型を確認できる
* 整数型（ `int` ）、浮動小数点型（ `float` ）、文字列型（ `str` ）、真理値型（ `bool` ）を使うことが多い
* `str` 関数、 `int` 関数などデータ型を変換するための関数も用意されている

---

### 演習

* [エクササイズ - 変数と演算子](../ex/02_basic_ex.md)

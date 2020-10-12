# 組み込み型 - str型

## str型

### `str1.py`

``` py
str = "Hello World!"
upper_str = str.upper()
print(upper_str)

lower_str = str.lower()
print(lower_str)
```

### 実行結果

``` 
$ python str1.py
HELLO WORLD!
hello world!
```

### 解説

* `upper` メソッドは文字列を大文字に変換する
* 小文字に変換する場合は `lower` メソッドを使う
* 大文字小文字を反転する場合は、 `swapcase` メソッドを使う

---

### `str2.py`

``` py
str = "hello world"
capitalize_str = str.capitalize()
print(capitalize_str)

title_str = str.title()
print(title_str)
```

### 実行結果

``` 
$ python str2.py
Hello world
Hello World
```

### 解説

* `capitalize` メソッドは先頭文字を大文字にする
* `title` メソッドは単語単位で先頭文字を大文字にする

---

### `str3.py`

``` py
str = "Hello World"

l_find = str.find("l")
print("l find:", l_find)
x_find = str.find("x")
print("x find:", x_find)

try:
    l_index = str.index("l")
    print("l index:", l_index)
    x_index = str.index("x")
    print("i index:", x_index)
except ValueError as e:
    print(e)

l_in_str = "l" in str
print("l in str:", l_in_str)
x_in_str = "x" in str
print("x in str:", x_in_str)
```

### 実行結果

``` 
$ python str3.py
l find: 2
x find: -1
l index: 2
substring not found
l in str: True
x in str: False
```

### 解説

* `find` メソッドは引数で指定した文字が、対象文字列の中で先頭から何文字目にあるかを返す（存在しない場合は `-1` を返す）
* `index` メソッドは引数で指定した文字が、対象文字列の中で先頭から何文字目にあるかを返す（存在しない場合は `ValueError` を返す）
* 指定した文字列が、対象文字列の中に存在するかどうかは `in` キーワードで判定できる

---

### `str4.py`

``` py
str = "Hello World"

print(str[0])
print(str[6:])
for char in str:
    print(char)
```

### 実行結果

``` 
$ python str4.py
H
World
H
e
l
l
o
 
W
o
r
l
d
```

### 解説

* Pythonの文字列はシーケンス（テキストシーケンス）と呼ばれる
* シーケンスとは「連続」や「順序」という意味で、データが並んでいるオブジェクトのこと
* Pythonの `str` 型のインスタンスは、リストやタプルのようにインデックスで部分文字列を取得できる

> Pythonの代表的なシーケンスには `list` 、 `tuple` 、 `range` があります。

---

### `str5.py`

``` py
names_str = "Alice,Bob,Charlie"
namses = names_str.split(",")
print(namses)
```

### 実行結果

``` 
$ python str5.py
['Alice', 'Bob', 'Charlie']
```

### 解説

* `split` メソッドは、引数に指定した区切り文字で配列に分割します。

---

### `str6.py`

``` py
names = ["Alice", "Bob", "Charlie"]
namses_str = "-".join(names)
print(namses_str)
```

### 実行結果

``` 
$ python str6.py
Alice-Bob-Charlie
```

### 解説

* `join` メソッドは、その文字列を区切り文字として、引数で受け取ったシーケンスを文字列に変換する

---

### `str7.py`

``` py
strs = ["12345", "ABCDE", "ABC12"]
for str in strs:
    print(str, str.isalpha())
```

### 実行結果

``` 
$ python str7.py
12345 False
ABCDE True
ABC12 False
```

### 解説

* `isalpha` メソッドは、その文字列がアルファベットかどうかを判定します。アルファベットの場合は戻り値に `True` そうでない場合は `False` を返します。

---

### `str8.py`

``` py
str = "Title: {0} Price: {1:,}"
title = "Python Book"
price = 3000

format_str = str.format(title, price)
print(format_str)

print(f"Title: {title} Price: {price:,}")
```

### 実行結果

``` 
$ python str8.py
Title: Python Book Price: 3000
Title: Python Book Price: 3000
```

### 解説

* `format` メソッドは、文字列の書式操作を行う
* `{}` で区切られた置換フィールドに引数で受け取った値を文字列を指定する
* 同様の操作はフォーマット文字列（ `f""` ）でも可能

---

## 演習

* [エクササイズ - str型](../ex/21_str_ex.md)

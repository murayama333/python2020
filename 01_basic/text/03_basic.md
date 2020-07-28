# 制御構文 - 分岐構造 - if文

### `if1.py`

``` python
point = 80

if point >= 50:
    print("Good")
```

### 実行

``` 
$ python if1.py
Good
```

### 解説

* if文によって分岐構造を定義できる
* ifの処理ブロックはインデントで表現する
* if文の構文が以下のとおり

``` 
if 条件式:
    条件式がTrueの場合の処理
else:
    条件式がFalseの場合の処理
```

---

### `if2.py`

``` python
point = 40

if point >= 50:
    print("Good")
else:
    print("Bad")
```

### 実行

``` 
$ python if2.py
Bad
```

### 解説

* if - else文によって条件式が不成立の場合の処理を定義できる
* elseブロックは省略可能
* if - else文の構文が以下のとおり

``` 
if 条件式:
    条件式がTrueの場合の処理
else:
    条件式がFalseの場合の処理
```

---

### `if3.py`

``` python
point = 80

if point >= 90:
    print("Great")
elif point >= 50:
    print("Good")
else:
    print("Bad")
```

### 実行

``` 
$ python if3.py
Good
```

### 解説

* elifキーワードによって複数の条件式を定義できる
* 定義した条件式は上から順に評価される
* if - elif - else文の構文が以下のとおり

``` 
if 条件式1:
    条件式1がTrueの場合の処理
elif 条件式2:
    条件式2がTrueの場合の処理
else:
    それ以外（条件式1,2がFalse）の場合の処理
```

---

### `if4.py`

``` python
math = 85
english = 90

if math >= 80 and english >= 80:
    print("Good")
else:
    print("Bad")
```

### 実行

``` 
> python if4.py
Good
```

### 解説

* 複数の条件式の組み合わせに論理演算子を使う
* 論理積 `and` （かつ）、論理和 `or` （あるいは）、否定 `not` を利用できる
* 論理演算子

``` 
if 条件式1 論理演算子 条件式2:
    条件が成立した場合の処理
```

---

### `if5.py`

``` python
a = 1
b = "1"
c = 1.0
d = True

print(a == b)
print(a == c)
print(a == d)
```

### 実行

``` 
$ python if5.py
False
True
True
```

### 解説

* `int` 型データと `float` 型データを比較できる
* `str` 型データは異なるデータ型と比較できない
* `int` 型データの `1` は `True` 、 `0` は `False` と等しい

---

### 演習

* [エクササイズ - 制御構文 - 分岐構造 - if文](../ex/03_basic_ex.md)

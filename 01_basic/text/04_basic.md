# 制御構文 - 反復構造 - while文

### `while1.py`

``` python
count = 0

while count < 5:
    print("*", end="")
    count = count + 1
```

### 実行

``` 
$ python while1.py 
*****
```

### 解説

* `while` 文によって反復構造を定義できる
* `while` の処理ブロックはインデントで表現する
* `while` 文の構文が以下のとおり

``` 
while 条件式:
    条件式がTrueの場合の処理
```

> `while` 文は `if` 文と異なり、条件式が `True` の間、インデントされた処理ブロックを繰り返し実行します。

---

### `while2.py`

``` python
total = 0
i = 1
while i <= 10:
    total = total + i
    i += 1

print(total)
```

### 実行

``` 
$ python while2.py
55
```

### 解説

* 反復を制御する変数をカウンター変数などと呼ぶ
* カウンター変数は `i` という名前を付けることが多い
* 変数の値を `1` 増やす操作をインクリメント、 `1` 減らす操作をデクリメントと呼ぶ

---

### `while3.py`

``` python
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1
```

### 実行

``` 
$ python while3.py 
1 2 3 4 5 6 7 8 9 
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36 
5 10 15 20 25 30 35 40 45 
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81 
```

### 解説

* `while` 文の中に `while` 文を定義することもできる
* このような入れ子構造をネストと呼ぶ
* 外側の反復構造のカウンター変数は `i` 、内側の反復構造のカウンター変数は `j` のように異なる名前を付ける

---

### 演習

* [エクササイズ - 制御構文 - 反復構造 - while文](../ex/04_basic_ex.md)

# Python基礎 実力テスト - Part1 - 追加問題

## `no41.py`

次のプログラムがあります。

``` py
# TODO def calc_item function
    

items = [{"price": 100, "count": 3},
         {"price": 200, "count": 2},
         {"price": 300, "count": 1}]
total = 0
for item in items:
    total += calc_item(**item)
print(f"{total:,}")
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
1,000
```

---

## `no42.py`

次のプログラムがあります。

``` py
# TODO def calc_item function 


# TODO def calc_total function


items = [{"price": 100, "count": 3},
         {"price": 200, "count": 2},
         {"price": 300, "count": 1}]
total = calc_total(items)
print(f"{total:,}")
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
1,000
```

---

## `no43.py`

次のプログラムがあります。

``` py
# def print_board function


print_board()
print_board(rows=3, columns=9)
print_board(rows=6, columns=4 ,symbol="=")
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
*****
*****
*****
*****
*****
*********
*********
*********
====
====
====
====
====
==== 
```

---

## `no44.py`

次のプログラムがあります。

``` py
scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
 90: 2
 95: 2
 80: 3
 85: 1
100: 1 
```

> 得点ごとの件数を表示します。

---

## `no45.py`

次のプログラムがあります。

``` py
scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Mode: 80
```

> 最頻値（出現回数の最も多いもの）を表示します。

---

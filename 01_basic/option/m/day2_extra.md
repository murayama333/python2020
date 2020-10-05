# Python基礎 実力テスト - Part2 - 追加問題

## `no46.py`

次のプログラムがあります。

``` py
names1 = ["Andy", "Betty", "Carol"]
names2 = ["Alice", "Bob", "Charlie"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Andy Alice
Betty Bob
Carol Charlie
```

---

## `no47.py`

次のプログラムがあります。

``` py
names = ["Andy", "Bob", "Carol", "Daniel", "Ellen"]
except_names = ["Andy", "Carol"]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
['Bob', 'Daniel', 'Ellen'] 
```

`names` リストの要素について、 `except_names` に存在しないものだけを表示します。

---

## `no48.py`

次のプログラムがあります。

``` py
# TODO def print_space_board function

print_space_board()
print_space_board(rows=3, columns=9)
print_space_board(rows=6, columns=4 ,symbol="=")

```

実行結果のとおり出力してください。

＜実行結果＞

``` 
*****
*   *
*   *
*   *
*****
*********
*       *
*********
====
=  =
=  =
=  =
=  =
```

---

## `no49.py`

次のプログラムがあります。

``` py
scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]
```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Median: 90
```

> 中央値（小さいものから順に並べたときに、中央にくる値）を表示します。

---

## `no50.py`

次のプログラムがあります。

``` py
# TODO def mean_median_mode function
    mean = sum(scores) // len(scores)
    mid = len(scores) // 2
    median = sorted(scores)[mid]

    score_dict = {}
    for score in scores:
        count = 1
        if score in score_dict.keys():
            count = score_dict[score]
            count = count + 1
        score_dict[score] = count
    mode = 0
    max_score_count = max(score_dict.values())
    for score, count in score_dict.items():
        if count == max_score_count:
            mode = score
            break
    return mean, median, mode

scores = [90, 95, 80, 85, 80, 95, 80, 90, 100]
mean, median, mode = mean_median_mode(scores)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

```

実行結果のとおり出力してください。

＜実行結果＞

``` 
Mean: 88
Median: 90
Mode: 80
```

> 平均値（ `Mean` ）、中央値（ `Median` ）、最頻値（ `Mode` ）を表示します。

---

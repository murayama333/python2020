# エクササイズ - 組み込み型 - range型

## `range_ex1.py`

``` py
my_range = range(10, 1, -1)

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python range_ex1.py
start: 10
stop: 1
step: -1
```

---

## `range_ex2.py`

``` py
class MyIterator:
    # TODO


names = ["Alice", "Bob", "Carol"]
for i, v in MyIterator(names):
    print(i, v)

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python range_ex2.py
0 Alice
1 Bob
2 Carol
```

---

## `range_ex3.py`

``` py
def odd_generator(start=1, stop=10):
    # TODO


og = odd_generator()
for v in og:
    print(v)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python range_ex3.py
1
3
5
7
9
```

---

### テキスト

* [テキスト - 組み込み型 - range型](../text/25_range.md)

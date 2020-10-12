# 組み込み型 - range型

## range型

### `range1.py`

``` py
my_range = range(1, 10)
print(my_range[5])
print(my_range.start)
print(my_range.stop)
print(my_range.step)
```

### 実行結果

``` 
$ python range1.py 
6
1
10
1
```

### 解説

* `range` 型はシーケンス型であるため要素番号でアクセスできる
* `range` 型には、 `start` 、 `stop` 、 `step` 3つのデータ属性がある

---

### `range2.py`

``` py
from memory_profiler import profile

@profile
def demo():
    for i in range(1, 1_000_000):
        pass

demo()
```

### 実行結果

``` 
$ python range2.py
Filename: /Users/your_name/Desktop/python/range2.py

Line #    Mem usage    Increment   Line Contents
================================================
     3     37.0 MiB     37.0 MiB   @profile
     4                             def demo():
     5     37.1 MiB      0.0 MiB       for i in range(1, 1_000_000):
     6     37.1 MiB      0.0 MiB           pass
```

### 解説

* `range` 型の オブジェクトはリストと異なり、要素にアクセスされたときに初めて生成される
* たとえば100万件の要素を持つリストはメモリを大量に消費するが、 `range` オブジェクトの場合はメモリの使用を節約できる

### 参考：100万件のリストをループする場合

> `for i in list(range(1, 1_000_000)):` とするとどうなるか比較してみましょう。

``` 
Filename: /Users/your_name/Desktop/python/range2.py

Line #    Mem usage    Increment   Line Contents
================================================
     3     37.0 MiB     37.0 MiB   @profile
     4                             def demo():
     5     75.7 MiB     38.6 MiB       for i in list(range(1, 1_000_000)):
     6     75.7 MiB      0.0 MiB           pass
```

> `memory_profiler` は別途インストールしておく必要があります。

---

### `range3.py`

``` py
class MyRange:
    def __init__(self, start, stop, step=1):
        self.index = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.stop:
            raise StopIteration()
        value = self.index
        self.index += 1
        return value

my_range = MyRange(1, 10)
for i in my_range:
    print(i)
```

### 実行結果

``` 
$ python range3.py
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

### 解説

* Pythonにはイテレータという仕組みが用意されている
* イテレータは"反復子"という意味で `__iter__` メソッドと `__next__` メソッドによって表現できる
* `for` 文の `in` 句にはイテレータを指定できる

> ここでは `range` を模倣したMyRangeクラスを作成しています。

---

### `range4.py`

``` py
def my_range(start, end, step=1):
    index = start
    while index < end:
        print("yield", index)
        yield index
        index += step

for i in my_range(1, 10):
    print(i)
```

### 実行結果

``` 
$ python range4.py
yield 1
1
yield 2
2
yield 3
3
yield 4
4
yield 5
5
yield 6
6
yield 7
7
yield 8
8
yield 9
9
```

### 解説

* Pythonには `range` のように必要になったデータをその場で生成する仕組みが用意されている
* このような仕組みをジェネレータと呼ぶ
* `yield` キーワードを使ってジェネレータを実装できる

---

## 演習

* [エクササイズ - range型](../ex/25_range_ex.md)

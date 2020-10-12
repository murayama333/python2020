# トレーニング - 組み込み型 - range型

## `range_tr1.py`

``` python
def count_down_generator():
    # TODO

for i in count_down_generator():
    print(i)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
5
4
3
2
1
0
```

> ジェネレータとして機能する `count_down_generator` 関数を定義します。

---

## `range_tr2.py`

``` python
def fizzbuzz_generator(start, stop):
    # TODO

for i in fizzbuzz_generator(1, 16):
    print(i)
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

---

## `range_tr3.py`

``` python
class AlphabetIterator:
    # TODO


for v in AlphabetIterator():
    print(v, end="")
print()
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

---

## `range_tr4.py`

``` python
class AlphabetIterator:
    # TODO


for v in AlphabetIterator(upper=True):
    print(v, end="")
print()

for v in AlphabetIterator(upper=False):
    print(v, end="")
print()
```

次の実行結果となるようにPythonプログラムを作成してください。

### 実行結果

``` 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
```

---

### テキスト

* [テキスト - 組み込み型 - range型](../text/25_range.md)

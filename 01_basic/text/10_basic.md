# データ構造 - リストの内包表記

### `lc1.py`

``` python
numbers = [i for i in range(10)]
print(numbers)
```

### 実行

``` 
$ python lc1.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 解説

* リストの内包表記とは、リストを簡単に作成する仕組み
* `[式 for 変数 in イテレート可能オブジェクト]` という文法で記述する
* イテレート可能オブジェクトには、リストやタプル、ディクショナリ、文字列などがある

### 参考

* `lc1.py` と同等のコードは次のようになる

``` python
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)
```

---

### `lc2.py`

``` python
numbers = [1, 2, 3, 4, 5]
numbers2 = [i * 2 for i in numbers]
print(numbers2)
```

### 実行

``` 
$ python lc2.py
[2, 4, 6, 8, 10]
```

### 解説

* リストの内包表記を使って既存のリストを加工して新たなリストを生成できる

---

### `lc3.py`

``` python
numbers = [1, 2, 3, 4, 5]
numbers2 = [i for i in numbers if i % 2 == 0]
print(numbers2)
```

### 実行

``` 
$ python lc3.py
[2, 4]
```

### 解説

* リストの内包表記を使って既存のリストをフィルタリングして新たなリストを生成できる

---

### `lc4.py`

``` python
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = [i * j for i in numbers1 for j in numbers2]
print(numbers3)
```

### 実行

``` 
$ python lc4.py
[10, 20, 30, 20, 40, 60, 30, 60, 90]
```

### 解説

* 内包表記内に複数の `for` 文を記述できる

### 参考

* `lc4.py` と同等のコードは次のようになる

``` python
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = []
for i in numbers1:
    for j in numbers2:
        numbers3.append(i * j)
print(numbers3)
```

---

### 演習

* [エクササイズ - リストの内包表記](../ex/10_basic_ex.md)

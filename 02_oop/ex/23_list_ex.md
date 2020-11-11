# エクササイズ - 組み込み型 - list型

## `list_ex1.py`

``` py
lst = [1, 2, 4, 5]

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python list_ex1.py
[1, 2, 3, 4, 5]
```

---

## `list_ex2.py`

``` py
lst = list(range(1, 4))

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python list_ex2.py
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

---

## `list_ex3.py`

``` py
names1 = ["Alice", "Bob", "Charlie"]
names2 = ["Andy", "Betty", "Carol"]

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python list_ex3.py
['Charlie', 'Carol', 'Bob', 'Betty', 'Andy', 'Alice']
```

---

## `list_ex4.py`

``` py
names1 = ["Alice", "Andy", "Betty", "Bob", "Carol", "Charlie"]
names2 = ["Andy", "Betty", "Carol"]

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python list_ex4.py
['Alice', 'Bob', 'Charlie']
```

> `names1` から `names2` を除いたものを表示します。

---

## `list_ex5.py`

``` py
names1 = ["Alice", "Andy", "Bob", "Carol"]
names2 = ["Alice", "Betty", "Carol", "Charlie"]

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python list_ex5.py
['Alice', 'Andy', 'Betty', 'Bob', 'Carol', 'Charlie']
```

> `names1` と `names2` を連結し、重複を排除したリストを表示します。

---

## `list_ex6.py`

``` py
numbers = [1, 2, 3, 4, 5]
while len(numbers) > 0:
    number = ???
    print(number)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python list_ex6.py
5
4
3
2
1
```

> `numbers` の要素を終端から1つずつ取得します。

---

### テキスト

* [テキスト - 組み込み型 - list型](../text/23_list.md)

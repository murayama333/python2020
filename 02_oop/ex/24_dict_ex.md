# エクササイズ - 組み込み型 - dict型

## `dict_ex1.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3}

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex1.py
{'key1': 1, 'key3': 3}
```

---

## `dict_ex2.py`

``` py
my_dict1 = {"key1": 1, "key2": 2, "key3": 3}
my_dict2 = {"key3": 30, "key4": 40, "key5": 50}

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex2.py
{'key1': 1, 'key2': 2, 'key3': 30, 'key4': 40, 'key5': 50}
```

---

## `dict_ex3.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
except_keys = ["key1", "key3", "key5"]

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex3.py
{'key2': 2, 'key4': 4}
```

> `my_dict` から `except_keys` のキーを除いたディクショナリを生成して表示します。

---

## `dict_ex4.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
while len(my_dict):
    key, value = ???
    print(key, value)
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex4.py
key5 5
key4 4
key3 3
key2 2
key1 1
```

> `my_dict` のキーと値を終端から1つずつ取得します。

---

## `dict_ex5.py`

``` py
keys = ["key1", "key2", "key3", "key4", "key5"]
value = 0

# TODO
```

次の実行結果となるようにプログラムを作成してください。

### 実行結果

``` 
$ python dict_ex5.py
{'key1': 0, 'key2': 0, 'key3': 0, 'key4': 0, 'key5': 0}
```

---

### テキスト

* [テキスト - 組み込み型 - dict型](../text/24_dict.md)

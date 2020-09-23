# エクササイズ - パッケージ

## ex01

次の `mycollection` パッケージがあります。

``` 
ex01
├── main.py
└── mycollection
    └── list.py
```

#### `ex01/mycollection/list.py`

``` py
def same_value_list(size=9, value=1):
    return [value for _ in range(size)]

def random_value_list(size=9, start=1, end=9):
    from random import randint
    return [randint(start, end) for _ in range(size)]
```

#### `ex01/main.py`

``` py
import ???

list1 = mycollection.list.same_value_list()
list2 = mycollection.list.random_value_list()
print(list1)
print(list2)
```

次の実行結果となるようにPythonプログラム（ `main.py` ）を作成してください。

### 実行結果

``` 
$ cd ex01
$ python main.py
[1, 1, 1, 1, 1, 1, 1, 1, 1]
[3, 5, 8, 8, 4, 7, 5, 3, 6]
```

> `random_value_list` 関数の戻り値はランダムな値になります。

---

## ex02

次の `mycollection` パッケージがあります。（ex01をコピーして作成します）

``` 
ex02
├── main.py
└── mycollection
    ├── dict.py
    └── list.py
```

> `dict.py` を追加し、 `main.py` を修正します。 `list.py` に変更はありません。

#### `ex02/mycollection/dict.py`

``` py
def same_value_dictionary(keys, value=1):
    ???

def random_value_dictionary(keys, start=1, end=9):
    ???
```

#### `ex02/main.py`

``` py
import mycollection.list as ???
import mycollection.dict as ???

list1 = myls.same_value_list()
list2 = myls.random_value_list()
print(list1)
print(list2)

keys = ["key1", "key2", "key3"]
dict1 = mydc.same_value_dictionary(keys)
dict2 = mydc.random_value_dictionary(keys)
print(dict1)
print(dict2)
```

次の実行結果となるようにPythonプログラム（ `dict.py` 、 `main.py` ）を作成してください。

### 実行結果

``` 
$ cd ../ex02
$ python main.py
[1, 1, 1, 1, 1, 1, 1, 1, 1]
[9, 4, 8, 5, 2, 1, 2, 1, 7]
{'key1': 1, 'key2': 1, 'key3': 1}
{'key1': 4, 'key2': 2, 'key3': 5}
```

> `random_value_list` 関数、 `random_value_dict` 関数の戻り値はランダムな値になります。

---

## ex03

次の `mycollection` パッケージがあります。（ex02をコピーして作成します）

``` 
ex03
├── 
└── mycollection
    ├── __init__.py
    ├── dict.py
    └── list.py
```

> `__init__.py` を追加し、 `main.py` を修正します。その他のファイルに変更はありません。

#### `ex03/mycollection/__init__.py`

``` py
???
???
```

> `dict.py` 、 `list.py` を読み込みます。

#### `ex03/main.py`

``` py
import mycollection

list1 = mycollection.list.same_value_list()
list2 = mycollection.list.random_value_list()
print(list1)
print(list2)

keys = ["key1", "key2", "key3"]
dict1 = mycollection.dict.same_value_dictionary(keys)
dict2 = mycollection.dict.random_value_dictionary(keys)
print(dict1)
print(dict2)
```

> `import mycollection` と記述します。

次の実行結果となるようにPythonプログラム（ `__init__.py` 、 `main.py` ）を作成してください。

### 実行結果

``` 
$ cd ../ex03
$ python main.py
[1, 1, 1, 1, 1, 1, 1, 1, 1]
[9, 4, 8, 5, 2, 1, 2, 1, 7]
{'key1': 1, 'key2': 1, 'key3': 1}
{'key1': 4, 'key2': 2, 'key3': 5}
```

> `random_value_list` 関数、 `random_value_dict` 関数の戻り値はランダムな値になります。

---

### テキスト

* [テキスト - パッケージ](../text/14_basic.md)

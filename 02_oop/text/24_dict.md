# 組み込み型 - dict型

## dict型

### `dict1.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3}
print(my_dict)

my_dict["key4"] = 4
print(my_dict)

value = my_dict.setdefault("key5", 5)
print(value)
print(my_dict)

value = my_dict.setdefault("key5", 55)
print(value)
print(my_dict)
```

### 実行結果

``` 
$ python dict1.py 
{'key1': 1, 'key2': 2, 'key3': 3}
{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}
5
{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
5
{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
```

### 解説

* `dict` 型の `setdefault` メソッドはディクショナリにキーと値を追加する
* ただし、すでにキーが存在する場合は値を上書きしない
* `setdefault` メソッドは戻り値に、指定したキーに関連する値を返す

---

### `dict2.py`

``` py
my_dict1 = {"key1": 1, "key2": 2, "key3": 3}
my_dict2 = {"key3": 33, "key4": 44, "key5": 55}
my_dict1.update(my_dict2)
print(my_dict1)
```

### 実行結果

``` 
$ python dict2.py
{'key1': 1, 'key2': 2, 'key3': 33, 'key4': 44, 'key5': 55}
```

### 解説

* `dict` 型の `update` メソッドは引数で受け取ったディクショナリを既存のディクショナリにマージする
* キーが競合する場合は引数で指定したディクショナリが優先される

---

### `dict3.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
try:
    value = my_dict["key1"]
    print(value, my_dict)
    value = my_dict["key10"]
    print(value, my_dict)
except KeyError as e:
    print(e)

value = my_dict.get("key1")
print(value, my_dict)
value = my_dict.get("key10", 10)
print(value, my_dict)

value = my_dict.pop("key1")
print(value, my_dict)

item = my_dict.popitem()
print(item, my_dict)
```

### 実行結果

``` 
$ python dict3.py
1 {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
'key10'
1 {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
10 {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
1 {'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
('key5', 5) {'key2': 2, 'key3': 3, 'key4': 4}
```

### 解説

* ディクショナリに存在しないキーを指定した場は `KeyError` が発生する
* `dict` 型の `get` メソッドは、引数で指定したキーが存在しない場合に `None` を返却する。また第2引数でキーが存在しない場合のデフォルト値を指定できる
* `dict` 型の `pop` メソッドはディクショナリから指定したキーに関連する値を取り出す（ディクショナリからキーと値は削除される）。 `popitem` メソッドはディクショナリの終端のキーと値をタプルで取り出す

---

### `dict4.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
keys = my_dict.keys()
print(keys)

values = my_dict.values()
print(values)

items = my_dict.items()
print(items)

my_list = list(my_dict)
print(my_list)
```

### 実行結果

``` 
$ python dict4.py
dict_keys(['key1', 'key2', 'key3', 'key4', 'key5'])
dict_values([1, 2, 3, 4, 5])
dict_items([('key1', 1), ('key2', 2), ('key3', 3), ('key4', 4), ('key5', 5)])
['key1', 'key2', 'key3', 'key4', 'key5']
```

### 解説

* `dict` 型の `keys` メソッドはキーの一覧を取得する（戻り値は `dict_keys` 型）
* `dict` 型の `values` メソッドはキーの一覧を取得する（戻り値は `dict_values` 型）
* `dict` 型の `items` メソッドはキーの一覧を取得する（戻り値は `items` 型）

> `list(my_dict)` とするとキーのリストに変換できる

---

### `dict5.py`

``` py
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
del my_dict["key1"]
print(my_dict)

my_dict.clear()
print(my_dict)
```

### 実行結果

``` 
$ python dict5.py
{'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
{}
```

### 解説

* `del`文でディクショナリから指定したキーと関連する値を削除できる
* `dict` 型の `clear` メソッドはディクショナリ内のすべてのキーと値を削除する

---

### `dict6.py`

``` py
keys = [f"key{i}" for i in range(1, 5)]
my_dict = dict.fromkeys(keys, 10)
print(my_dict)
```

### 実行結果

``` 
$ python dict6.py
{'key1': 10, 'key2': 10, 'key3': 10, 'key4': 10}
```

### 解説

* `dict` 型の `fromkeys` メソッドはキーのリストからディクショナリを生成する
* `dict` 型の `fromkeys` メソッドはクラスメソッドである

---

## 演習

* [エクササイズ - dict型](../ex/24_dict_ex.md)

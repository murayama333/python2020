# データ構造 - ディクショナリ

### `dict1.py`

``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
print(cities["Osaka"])
print(cities["Sakai"])
print(cities["Higashiosaka"])
```

### 実行

``` 
$ python dict1.py 
270
84
50
```

### 解説

* ディクショナリは `キー` と `値` のペアでデータを管理する
* Pythonのディクショナリは `{}` の中に `キー` と `値` を `:` で並べて記述する
* `キー` には様々な型のデータを利用できますが文字列を使うことが多い

---

### `dict2.py`

``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
length = len(cities)
print(length)
```

### 実行

``` 
$ python dict2.py
3
```

### 解説

* ディクショナリの要素数（キーと値の組み合わせの数）を求めるには `len` 関数を使う

---

### `dict3.py`


``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
cities["Hirakata"] = 40
print(cities)
```

### 実行

``` 
$ python dict3.py 
{'Osaka': 270, 'Sakai': 84, 'Higashiosaka': 50, 'Hirakata': 40}
```

### 解説

* 存在しないキーを指定することで、ディクショナリに要素を追加できる

---

### `dict4.py`

``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
cities["Osaka"] = 264
print(cities)
```

### 実行

``` 
$ python dict4.py
{'Osaka': 264, 'Sakai': 84, 'Higashiosaka': 50}
```

### 解説

* 既存のキーを指定することで、ディクショナリの要素を更新できる


---

### `dict5.py`

``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}

for key in cities:
    print(key)
```

### 実行

``` 
$ python dict5.py
Osaka
Sakai
Higashiosaka
```

### 解説

* ディクショナリを `for` 文を使って処理することができる

> ディクショナリを `for` 文で処理するとディクショナリの `キー` にアクセスできる

---

### `dict5_2.py`

``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}

for value in cities.values():
    print(value)
```

### 実行

``` 
$ python dict5_2.py
270
84
50
```

### 解説

* `for` 文の中でディクショナリの `値` にアクセスするには、ディクショナリ変数の `values` メソッドを呼び出して `値` のリストに変換する

---

### `dict5_3.py`

``` python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}

for key, value in cities.items():
    print(key, value)
```

### 実行

``` 
$ python dict5_3.py
Osaka 270
Sakai 84
Higashiosaka 50
```

### 解説

* `for` 文の中でディクショナリの `キー` と `値` にアクセスするには、ディクショナリ変数の `items` メソッドを呼び出して `キー` と `値` のリストに変換する

---

### 演習

* [エクササイズ - データ構造 - ディクショナリ](../ex/07_basic_ex.md)

# データ構造 - リスト

### `list1.py`

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
print(cities[0])
print(cities[1])
print(cities[2])
```

### 実行

``` 
$ python list1.py
Osaka
Sakai
Higashiosaka
```

### 解説

* リストは一つの変数で複数のデータを管理する仕組み
* リストに含まれる一つひとつのデータを要素と呼ぶ
* 要素には先頭から要素番号（0から始まる番号）が割り振られている

> 要素番号のことを添え字やインデックスなどと呼びます。


### `list1_2.py`


``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
print(cities)
```

### 実行

``` 
$ python list1_2.py
['Osaka', 'Sakai', 'Higashiosaka']
```

### 解説

* Pythonのリストは`print`関数で出力するとリスト全体が表示される


### `list1_3.py`

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
print(cities[0:2])
print(cities[1:])
print(cities[:2])
```

### 実行

``` 
$ python list1_3.py
['Osaka', 'Sakai']
['Sakai', 'Higashiosaka']
['Osaka', 'Sakai']
```

### 解説

* Pythonのリストは `:` を使ったスライス指定（範囲指定）が可能

---

### `list2.py`

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
length = len(cities)
print(length)
```

### 実行

``` 
$ python list2.py
3
```

### 解説

* リストの要素数を求めるには `len` 関数を使う

---

### `list3.py`

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
length = len(cities)
for i in range(length):
    print(cities[i])
```

### 実行

``` 
$ python list3.py
Osaka
Sakai
Higashiosaka
```

### 解説

* リストは `for` 文を使ってループで処理できる
* リストの要素番号に `for` 文のカウンター変数（一般的には `i` ）を使う
* リストの要素番号は `0` から始まる点に注意する

### `list3_2.py`

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
for city in cities:
    print(city)
```

### 実行

``` 
$ python list3_2.py
Osaka
Sakai
Higashiosaka
```

### 解説

* for文の `in` 句にはリスト変数を指定できる

> `list3.py` に比べて `list3_2.py` の方が一般的な書き方です。

---

### `list4.py`

``` python
cities = []
cities.append("Osaka")
cities.append("Sakai")
cities.append("Higashiosaka")

print(cities)
```

### 実行

``` 
$ python list4.py
['Osaka', 'Sakai', 'Higashiosaka']
```

### 解説

* リスト変数のappendメソッドを使うことでリストに要素を追加できる

---

### `list5.py`

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
print(cities)

cities[0] = "Hirakata"
print(cities)
```

### 実行

``` 
$ python list5.py 
['Osaka', 'Sakai', 'Higashiosaka']
['Hirakata', 'Sakai', 'Higashiosaka']
```

### 解説

* リストに対して要素番号を指定することで、リストの要素を更新できる

---

### 演習

* [エクササイズ - データ構造 - リスト](../ex/06_basic_ex.md)

# データ構造 - リスト

### list1.py

* リストは一つの変数で複数のデータを管理する仕組み
* リストに含まれる一つひとつのデータを要素と呼ぶ
* 要素には先頭から要素番号（0から始まる番号）が割り振られている

> 要素番号のことを添え字やインデックスなどと呼びます。

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

### list1_2.py

* Pythonのリストはprint関数で出力するとリスト全体が表示される

``` python
cities = ["Osaka", "Sakai", "Higashiosaka"]
print(cities)
```

### 実行

``` 
$ python list1_2.py
['Osaka', 'Sakai', 'Higashiosaka']
```

### list1_3.py

* Pythonのリストは `:` を使ったスライス指定が可能

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

---

### list2.py

* リストの要素数を求めるには `len` 関数を使う

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

---

### list3.py

* リストは `for` 文を使ってループで処理できる
* リストの要素番号に `for` 文のカウンター変数（一般的には `i` ）を使う
* リストの要素番号は `0` から始まる点に注意する

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

### list3_2.py

* for文の `in` 句にはリスト変数を指定できる

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

> `list3.py` に比べて `list3_2.py` の方が一般的な書き方です。

---

### list4.py

* リスト変数のappendメソッドを使うことでリストに要素を追加できる

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

---

### list5.py

* リストに対して要素番号を指定することで、リストの要素を更新できる

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

---

### 演習

* [エクササイズ - データ構造 - リスト](../ex/06_basic_ex.md)

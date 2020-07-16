# リスト

### list1.py

+ リストは一つの変数で複数のデータを管理する仕組みです。
+ リストに含まれる一つひとつのデータを要素と呼びます。
+ 要素には先頭から要素番号（0から始まる番号）が割り振られています。

> 要素番号のことを添え字やインデックスなどと呼びます。

```python
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

+ Pythonのリストはprint関数で出力するとリスト全体が表示されます。

```python
cities = ["Osaka", "Sakai", "Higashiosaka"]
print(cities)
```

### 実行

```
$ python list1_2.py 
['Osaka', 'Sakai', 'Higashiosaka']
```

### list1_3.py

+ Pythonのリストは`:`を使ったスライス指定が可能です。

```python
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

+ リストの要素数を求めるには`len`関数を使います。

```python
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

+ リストは`for`文を使ってループで処理できます。
+ リストの要素番号に`for`文のカウンター変数（`i`）を使います。
+ リストの要素番号は`0`から始まる点に注意します。

```python
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

+ for文の`in`句にはリスト変数を指定します。

```python
cities = ["Osaka", "Sakai", "Higashiosaka"]
for city in cities:
  print(city)
```

### 実行

```
$ python list3.py
Osaka
Sakai
Higashiosaka
```

> `list3.py`に比べて`list3_2.py`の方が一般的な書き方です。

---


### list4.py

+ リスト変数のappendメソッドを使うことでリストに要素を追加できます。

```python
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

+ リストに対して要素番号を指定することで、リストの要素を更新できます。

```python
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

+ [エクササイズ - リスト](ex/06_basic_ex.md)
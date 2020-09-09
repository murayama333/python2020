# データ構造 - タプル

### `tuple1.py`

``` python
cities = ("Osaka", "Sakai", "Higashiosaka")
print(cities[0])
print(cities[1])
print(cities[2])
```

### 実行

``` 
$ python tuple1.py
Osaka
Sakai
Higashiosaka
```

### 解説

* タプルは、リストと同じように一つの変数で複数のデータを管理する仕組みで
* 要素には先頭から要素番号（0から始まる番号）が割り振られている
* タプルはリストと異なり、一度作成すると要素の追加、入れ替え、削除ができない


### `tuple1_2.py`

``` python
cities = ("Osaka", "Sakai", "Higashiosaka")
print(cities)
```

### 実行

``` 
$ python tuple1_2.py
('Osaka', 'Sakai', 'Higashiosaka')
```

### 解説

* Pythonのタプルはprint関数で出力するとタプル全体が表示される


### `tuple1_3.py`

``` python
cities = ("Osaka", "Sakai", "Higashiosaka")
print(cities[0:2])
print(cities[1:])
print(cities[:2])
```

### 実行

``` 
$ python tuple1_3.py
('Osaka', 'Sakai')
('Sakai', 'Higashiosaka')
('Osaka', 'Sakai')
```

### 解説

* Pythonのタプルは `:` を使ったスライス指定が可能

---

### `tuple2.py`

``` python
cities = ("Osaka", "Sakai", "Higashiosaka")
length = len(cities)
print(length)
```

### 実行

``` 
$ python tuple2.py
3
```

### 解説

* タプルの要素数を求めるには `len` 関数を使う

---

### `tuple3.py`


``` python
cities = ("Osaka", "Sakai", "Higashiosaka")
for city in cities:
    print(city)
```

### 実行

``` 
$ python tuple3.py
Osaka
Sakai
Higashiosaka
```

### 解説

* タプルは `for` 文を使ってループで処理できる

---

### `tuple4.py`

``` python
cities = ("Osaka", "Sakai", "Higashiosaka")
print(cities)

cities[0] = "Hirakata"
print(cities)
```

### 実行

``` 
$ python tuple4.py 
('Osaka', 'Sakai', 'Higashiosaka')
Traceback (most recent call last):
  File "tuple4.py", line 4, in <module>
    cities[0] = "Hirakata"
TypeError: 'tuple' object does not support item assignment
```

> 既存のタプルに新たなオブジェクトを割り当てることはできません。

### 解説

* タプルは一度作成すると要素の追加、入れ替え、削除ができない

---

### 演習

* [エクササイズ - データ構造 - タプル](../ex/09_basic_ex.md)

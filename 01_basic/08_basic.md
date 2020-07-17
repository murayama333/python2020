# タプル

### tuple1.py

+ タプルは、リストと同じように一つの変数で複数のデータを管理する仕組みです。
+ 要素には先頭から要素番号（0から始まる番号）が割り振られています。
+ タプルはリストと異なり、一度作成すると要素の追加、入れ替え、削除ができないようになっています。

```python
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

### tuple1_2.py

+ Pythonのタプルはprint関数で出力するとタプル全体が表示されます。

```python
cities = ("Osaka", "Sakai", "Higashiosaka")
print(cities)
```

### 実行

```
$ python tuple1_2.py
('Osaka', 'Sakai', 'Higashiosaka')
```

### tuple1_3.py

+ Pythonのタプルは`:`を使ったスライス指定が可能です。

```python
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

---

### tuple2.py

+ タプルの要素数を求めるには`len`関数を使います。

```python
cities = ("Osaka", "Sakai", "Higashiosaka")
length = len(cities)
print(length)
```

### 実行

```
$ python tuple2.py
3
```

---


### tuple3.py

+ タプルは`for`文を使ってループで処理できます。

```python
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

---

### tuple4.py

+ タプルは一度作成すると要素の追加、入れ替え、削除ができません。

```python
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

---

### 演習

+ [エクササイズ - タプル](ex/08_basic_ex.md)
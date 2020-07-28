# データ構造 - ディクショナリ

### dict1.py

+ ディクショナリは`キー`と`値`のペアでデータを管理する
+ Pythonのディクショナリは`{}`の中に`キー`と`値`を `:` で並べて記述する
+ `キー`には様々な型のデータを利用できますが文字列を使うことが多い

```python
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

---


### dict2.py

+ ディクショナリの要素数（キーと値の組み合わせの数）を求めるには`len`関数を使う

```python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
length = len(cities)
print(length)
```

### 実行

```
$ python dict2.py
3
```

---


### dict3.py

+ 存在しないキーを指定することで、ディクショナリに要素を追加できる

```python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
cities["Hirakata"] = 40
print(cities)
```

### 実行

```
$ python dict3.py 
{'Osaka': 270, 'Sakai': 84, 'Higashiosaka': 50, 'Hirakata': 40}
```

---

### dict4.py

+ 既存のキーを指定することで、ディクショナリの要素を更新できる

```python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}
cities["Osaka"] = 264
print(cities)
```

### 実行

```
$ python dict4.py
{'Osaka': 264, 'Sakai': 84, 'Higashiosaka': 50}
```

---

### dict5.py

+ ディクショナリを`for`文を使って処理することができる

```python
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

> ディクショナリを`for`文で処理するとディクショナリの`キー`にアクセスできる

---

### dict5_2.py

+ `for`文の中でディクショナリの`値`にアクセスするには、ディクショナリ変数の`values`メソッドを呼び出して`値`のリストに変換する

```python
cities = {"Osaka": 270, "Sakai": 84, "Higashiosaka": 50}

for key in cities.values():
    print(key)
```

### 実行

```
$ python dict5_2.py
270
84
50
```

---

### dict5_3.py

+ `for`文の中でディクショナリの`キー`と`値`にアクセスするには、ディクショナリ変数の`items`メソッドを呼び出して`キー`と`値`のリストに変換する

```python
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

---

### 演習

+ [エクササイズ - データ構造 - ディクショナリ](ex/07_basic_ex.md)
